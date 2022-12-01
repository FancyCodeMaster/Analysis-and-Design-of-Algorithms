# Implementing Binary Search Iteratively

def binary_search(arr , length , element):

    low = 0
    high = length -1 

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > element:
            high = mid -1
        elif arr[mid] < element:
            low = mid + 1
        else:
            return mid


arr_to_search = [1 , 2 , 3 , 8 , 27 , 88 , 227 , 277 , 772]
element_to_search = 227

element_index = binary_search(arr_to_search , len(arr_to_search) , element_to_search)
print("element" , element_to_search , "is found at index" , element_index)