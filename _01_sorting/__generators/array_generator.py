"""Generates an array with random elements
"""

import random   #library for generating random numbers
import sys      #library for getting system values

def generate_array(size: int, min_val=-sys.maxsize-1, max_val=sys.maxsize) -> list:
    """
    Generates an array of random elements with a given size

    Keyword arguments:
        size    -- int: number of elements of the array to be generated
        min_val -- int: minimum value of the elements to be generated
        max_val -- int: maximum value of the elements to be generated
    Return: 
        arr -- list:  array of numbers with a length equal to size
    """
    #raise type error if size is not int
    if type(size) is not int:
        raise TypeError("The size of the array should be of int data type.")
    
    #raise value error if size is less than or equal to zero 
    if size <= 0:
        raise ValueError("The size of the array should be greater than zero.")

    #initiate an empty array
    arr = []

    #generate randoms numbers whose value is between minimum and maximum value
    #then append them to the array
    #repeat this so that the lenght of the array is equal to the required size
    for _ in range(size):
        arr.append(random.randint(min_val, max_val))

    return arr
