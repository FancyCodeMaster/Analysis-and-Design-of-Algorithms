# Implementation of binary search recursively
import math

# returning value from a recursive function in python returns None instead of the value you desired
# it does so because the inner function does return the value but the main function seems to return the value from the first caller thus returning
# the None instead of the value of the last caller

# so better to print the index and the value at the exact condition you want

def binary_search(arr , low , high , element):
    #base case
    if low == high:
        print("element" , element , "found at position" , low)
    else:
        mid = math.floor((low+high) / 2)
        if arr[mid] > element:
            binary_search(arr , low , mid-1 , element)
        elif arr[mid] == element:
            print("element" , element , "found at position" , mid)
        else:
            binary_search(arr , mid+1 , high , element)

arr_to_search = [1 , 2 , 3 , 6 , 7 , 8 , 11 , 18 , 24]

binary_search(arr_to_search , 0 , len(arr_to_search)-1 , 8)

