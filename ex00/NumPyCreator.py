#!/bin/python3

import numpy as np


class NumpyCreator:
    def from_list(self, lst, datatype=None):
        if not lst or not isinstance(lst, list):
            return

        for element in lst:
            if len(element) != len(lst[0]):
                return

        return np.array(lst, dtype=datatype)

    def from_tuple(self, tpl, datatype=None):
        if not tpl or not isinstance(tpl, tuple):
            return

        for element in tpl:
            if len(element) != len(tpl[0]):
                return

        return np.array(tuple, dtype=datatype)

    def from_iterable(self, itr, datatype=None):
        if not itr:
            return
        try:
            iter(itr)
        except:
            return

        return np.array(itr, dtype=datatype)

    def from_shape(self, shape, value=0, datatype=None):
        if not shape or not isinstance(shape, tuple) or len(shape) != 2:
            return

        return np.full(shape, value)

    def random(self, shape, datatype=None):
        if not shape or not isinstance(shape, tuple) or len(shape) != 2:
            return

        return np.random.rand(shape[0], shape[1])

    def identity(self, n):
        if not isinstance(n, int):
            return
        return np.identity(n)


npc = NumpyCreator()
print(npc.from_list([[1, 2, 3], [6, 3, 4]]))

print(npc.from_list([[1, 2, 3], [6, 4]]))

print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))

print(npc.from_tuple(("a", "b", "c")))

print(npc.from_tuple(["a", "b", "c"]))

print(npc.from_iterable(range(5)))

shape = (3, 5)
print(npc.from_shape(shape))

print(npc.random(shape))

print(npc.identity(4))
