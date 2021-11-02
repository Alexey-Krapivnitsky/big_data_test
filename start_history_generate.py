from test_history import *


def main():
    test_history = History()
    history_file = 'test_history'

    def write_history(limit=3):
        while True:
            sequence = np.random.randint(0, 1000000, size=(1, 500))
            score = random.uniform(-100, 100)
            test_history.set_history(sequence, score)
            # print(test_history.history_arr.nbytes / 1073741824)
            if test_history.history_arr.nbytes / 1073741824 > limit:
                duplicate_count = test_history.duplicate
                test_history.save_history(history_file)
                return duplicate_count

    def start_generate(step_count, limit):
        for step in range(step_count):
            start = timeit.default_timer()
            dupe_count = write_history(limit)
            print(f'duplicate count = {dupe_count}')
            end = timeit.default_timer() - start
            print(f'execution time step {step + 1} = {end} seconds')
            test_history.history_arr = test_history.load_history(history_file)
            limit += 2

    start_generate(2, 3)


if __name__ == '__main__':
    main()
