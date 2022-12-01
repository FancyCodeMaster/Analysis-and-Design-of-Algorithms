# Implementation of binary search recursively
import math

def binary_search(arr , low , high , element):
    #base case
    if low == high:
        return low
    else:
        mid = math.floor((low+high) / 2)
        print("mid is" , mid)
        if arr[mid] > element:
            binary_search(arr , low , mid-1 , element)
        elif arr[mid] == element:
            return mid
        else:
            binary_search(arr , mid+1 , high , element)
        print("low is" , low , "high is" , high)

arr_to_search = [1 , 2 , 100 , 500 , 699 , 789 , 897]

print(binary_search(arr_to_search , 0 , len(arr_to_search)-1 , 2))
