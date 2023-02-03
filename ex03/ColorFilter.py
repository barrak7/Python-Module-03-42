#!/bin/python3

import numpy as np
import matplotlib as plt
from ImageProcessor import ImageProcessor as imp

class ColorFilter:
	def invert(self, array):
		"""
		Inverts the color of the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		try:
			arr = array.copy()
			arr[:,:,:3] = 1 - arr[:,:,:3]
			return arr
		except:
			return

	def to_blue(self, array):
		"""
		Applies a blue filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		try:
			arr = array.copy()
			arr[:,:,:2] = 0
			return arr
		except:
			return

	def to_green(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		try:
			arr = array.copy()
			arr[:,:,0] = 0
			arr[:,:,2] = 0
			return arr
		except:
			return

	def to_red(self, array):
		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
			Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		try:
			arr = array.copy()
			arr[:,:,1:3] = 0
			return arr
		except:
			return

	def to_celluloid(self, array):
		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
			celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
			Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		try:
			arr = array.copy()
			lvl = np.linspace(0, 255, num=5, endpoint=False)
			if arr.dtype == np.uint16:
				arr /= 256
				arr = arr.astype(np.uint8)

			elif arr.dtype == np.float32:
				arr *= 255
				arr = arr.astype(np.uint8)

			indec_arr = arr.copy()
			if (arr.shape[2] == 4):
				alpha = arr[:,:,3].copy()
			for value in lvl:
				arr[indec_arr > value] = value
			if (arr.shape[2] == 4):
				arr[:,:,3] = alpha
			return arr
		except:
			return


	def to_grayscale(self, array, filter, **kwargs):
		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = 'mean'/'m': performs the mean of RBG channels.
		For filter = 'weight'/'w': performs a weighted mean of RBG channels.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
			filter: string with accepted values in ['m','mean','w','weight']
			weights: [kwargs] list of 3 floats where the sum equals to 1,
			corresponding to the weights of each RBG channels.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		try:
			ro, col = array.shape[0], array.shape[1]
			arrsum = np.sum(array[:,:,:3], axis=2) / 3
			arrsum = arrsum.reshape(ro, col, 1)
			arrsum = np.broadcast_to(arrsum, (ro, col, 3))
			arr = array.copy()
			arr[:,:,:3] = arrsum
			if filter in ['m', 'mean']:
				return arr
			elif filter in ['w', 'weight']:
				weights = list(kwargs.keys())[0]
				weights = kwargs[weights]
				if (len(weights) != 3) or sum(weights) != 1:
					return
				weights = np.array(weights)
				arr[:,:,:3] = arr.astype(np.float64) * weights
				return arr
		except:
			return

