"""Bubble Sort"""

def bubble_sort(arr: list) -> list:
    """
    Sort array using bubble sort algorithim
    argumment:
        arr -- list: array to be sorted
    return:
        arr -- list: sorted array
    """
    steps = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            steps += 1

    print(f"Number of steps = {steps}")
    return arr
    