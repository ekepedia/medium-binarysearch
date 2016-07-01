def binarysearch ():
    array = [1,5,8,12,16,21,34,54,63,71,81,]
    target = 16
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
