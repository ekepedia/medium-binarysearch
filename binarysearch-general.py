def binarysearch (array, target):
    min = 0
    max = len(array) - 1

    while min <= max:
         median = int( (max + min)/2 )
         if array[median] == target:
             return median
         elif array[median] < target:
             min = median + 1
         elif array[median] > target:
             max = median -1

    return -1
