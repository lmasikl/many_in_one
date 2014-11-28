# coding=utf-8
import os
import sys
import re

__author__ = 'maxim'
__project__ = 'many_in_one'
__version__ = '0.0.1'


def to_period(array):
    """
    Change increasing values in array on index values
    >>> to_period(range(1, 6)) == 5 * [1]
    True
    """
    for i, a in enumerate(array):
        if not i:
            continue
        array[i] -= sum(array[:i])
    return array


def to_increase(array):
    """
    Change index values in array on increasing values
    >>> to_increase(5 * [1]) == range(1, 6)
    True
    """
    for i, a in enumerate(array):
        if not i:
            continue
        array[i] += array[i - 1]
    return array


def change(array):
    """
    >>> a = range(1, 6)
    >>> change(a)
    [1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5]
    """
    print(to_period(array))
    print(to_increase(array))

if __name__ == '__main__':
    change(range(1, 6))