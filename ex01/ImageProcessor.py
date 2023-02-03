#!/bin/python3

import matplotlib.pyplot as plt
import numpy as np


class ImageProcessor:
    @staticmethod
    def load(path):
        try:
            img = plt.imread(path)
            print(f"Image dimensions: {img.shape[0]} x {img.shape[1]}")
            return img
        except:
            print("Couldn't load Image.")

    @staticmethod
    def display(array):
        if not isinstance(array, np.ndarray):
            return
        try:
            plt.imshow(array)
            plt.show()
        except:
            print("Something went wrong")

