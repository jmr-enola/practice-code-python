Title: Bubble Sort

Description:
    A program for sorting array using bubble sort algorithm

How it works:
    Given an array [8, 2, 15, 6, 0] for example
    When I use the program to sort the given array
    Then the element of the resulting array will be arranged from least to greatest [0, 2, 6, 8, 15]

Algorithm:
- step 1 : start with the first element (current pos = 0).
- step 2 : if the current element is greater than the next element swap thier positions.
- step 3A: if the current position is less than the last position minus 1 then move to the next element (current pos + 1) and repeat step 2
- step 3B: if the current position is equal to the last position minus 1 and atleast one swapping was done then start again from step 1. Otherwise, do step 4.
- step 4 : return value of sorted array

Time Complexity: max = O(n^2), min = O(n-1)

Notes: Good for small sample sets.