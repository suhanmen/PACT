"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""



def reverse_Array_Upto_K(arr, k):
    if k > len(arr):
        return 'K is greater than the length of the array'
    return arr[:k][::-1] + arr[k:]

# Example usage
# reversed_array = reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4)
# print(reversed_array)  # Output: [4, 3, 2, 1, 5, 6]
