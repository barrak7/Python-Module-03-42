#!/bin/python3

import numpy as np


class ScrapBooker:
    def crop(self, array, dim, position=(0, 0)):
        """
                Crops the image as a rectangle via dim arguments (being the new height
                and width of the image) from the coordinates given by position arguments.
                Args:
                -----
                        array: numpy.ndarray
                        dim: tuple of 2 integers.
                        position: tuple of 2 integers.
                Return:
                -------
                        new_arr: the cropped numpy.ndarray.
                        None (if combinaison of parameters not compatible).
                Raise:
                ------
                        This function should not raise any Exception.
                """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) or not isinstance(position, tuple):
            print("Invalid parameters passed")
            return
        if len(dim) != 2 or len(position) != 2:
            print("Invalid parameters passed")
            return
        try:
            return array[position[0]:dim[0]+position[0], position[1]:dim[1]+position[1]]
        except:
            print("Invalid parameters passed")
            return

    def thin(self, array, n, axis):
        """
            Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
            Args:
            -----
                array: numpy.ndarray.
                n: non null positive integer lower than the number of row/column of the array
                (depending of axis value).
                axis: positive non null integer.
            Return:
            -------
                new_arr: thined numpy.ndarray.
                None (if combinaison of parameters not compatible).
            Raise:
            ------
                This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int):
            print("Invalid parameters passed!")
            return
        if n <= 0 or (axis != 0 and axis != 1):
            print("Invalid parameters passed!")
        try:
            new_arr = np.array(array)
            if axis == 1:
                new_arr = np.delete(new_arr, [i - 1 for i, e in enumerate(new_arr.T, 1) if i % n == 0], axis)
            else:
                new_arr = np.delete(new_arr, [i - 1 for i, e in enumerate(new_arr, 1) if i % n == 0], axis)
            return new_arr
        except:
            print("Something went wrong")
            return



    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
        -------
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int) or (axis != 0 and axis != 1):
            print("Invalid parameters passed!")
            return
        try:
            return np.repeat(array, n, axis)
        except:
            print("Something went wrong!")

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
                array: numpy.ndarray.
                dim: tuple of 2 integers.
        Return:
        -------
                new_arr: mosaic numpy.ndarray.
                None (combinaison of parameters not compatible).
        Raises:
        -------
                This function should not raise any Exception.
        """
        try:
            return np.tile(array, dim)
        except:
            print("Something went wrong!")
