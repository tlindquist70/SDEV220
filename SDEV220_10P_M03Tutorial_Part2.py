#Tracie Lindquist
#SDEV220_10P_M03_Tutorial_Part 2
#Create a program using a binary search to find a specific value in a sorted array 

#function to sort array in ascending order
def sort_array(unsorted_array):
    sorted_array = sorted(unsorted_array, key=lambda x: int(x))
    print(sorted_array)
    return sorted_array

#binary search function to fine specified value in the array
def binary_search(arr, array_size, element):
    low = 0
    mid = 0
    high = array_size-1
		
    while high >= low:
        mid = (high + low) // 2
        if arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid -1
        else:
            return mid

#functional code

#define variables
unsorted_array = [0,5,7,9,12,15,20,17,16]
sorted_array = []
array_size = len(unsorted_array)
element = 15

#call functions
sorted_array = sort_array(unsorted_array)
result = binary_search(sorted_array, array_size, element)

#return results
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
