"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

def bubble_sort(arr: list) -> list:
    """sumary_line"""
    
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