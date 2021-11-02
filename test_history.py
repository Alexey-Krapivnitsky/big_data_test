import random
import timeit

import numpy as np


class History:

    def __init__(self):
        self.score = None
        self.history_arr = None
        self.duplicate = 0

    def set_history(self, sequence, score):
        if self.history_arr is None:
            self.history_arr = sequence
        else:
            if self.is_it_dupe_sequence(sequence):
                if score < self.score:
                    self.score = score
                self.duplicate += 1
            else:
                self.history_arr = np.append(self.history_arr, sequence, axis=0)

    def is_it_dupe_sequence(self, sequence):
        result = np.where(self.history_arr == sequence)
        if result[0].size > 0:
            for elem in result[0]:
                if np.array_equal(self.history_arr[elem], sequence):
                    return True
        return False

    def save_history(self, filepath):
        np.save(filepath, self.history_arr)

    @staticmethod
    def load_history(filepath):
        filepath = filepath + '.npy'
        history = np.load(filepath)
        return history
