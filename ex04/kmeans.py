#!/bin/python3

import numpy as np
import pandas as pd
import random


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    @staticmethod
    def normalize(col):
        return (col - col.min()) / (col.max() - col.min())

    def set_centroids(self, arr):
        for i, centroid in enumerate(self.centroids):
            in_arr = arr[:, 0] == i
            if arr[in_arr].shape[0] == 0:
                self.centroids[i] = arr[random.randint(0, arr.shape[0]-1)]
                self.centroids[i][0] = i
                continue
            self.centroids[i] = np.sum(arr[in_arr], axis=0)
            self.centroids[i] /= arr[in_arr].shape[0]
            self.centroids[i][0] = i

    @staticmethod
    def get_distance(point, centroid):
        return (np.sqrt(np.sum((point[1:] - centroid[1:]) ** 2)))

    def cluster(self, point):
        distance = self.get_distance(point, self.centroids[0])
        for i, centroid in enumerate(self.centroids):
            new_dist = self.get_distance(point, centroid)
            if new_dist < distance:
                point[0] = i
                distance = new_dist

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
                X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
                None.
        Raises:
        -------
                This function should not raise any Exception.
        """
        if not isinstance(X, np.ndarray):
            return
        X = np.apply_along_axis(self.normalize, 0, X)
        self.centroids = X[np.random.choice(
            X.shape[0], self.ncentroid, replace=False), :]
        i = self.max_iter
        while (i):
            for e, point in enumerate(X):
                self.cluster(X[e])
            self.set_centroids(X)
            i -= 1

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
                X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
                the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
                This function should not raise any Exception.
        """
        arr = []
        for point in X:
            distance = self.get_distance(point, self.centroids[0])
            for i, centroid in enumerate(self.centroids):
                new_dist = self.get_distance(point, centroid)
                if new_dist < distance:
                    arr.append(i)
        return (np.array(arr))
