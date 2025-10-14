"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""



def split_Arr(arr, n):
    return arr[n:] + arr[:n]

# Example usage
# split_Arr([12,10,5,6,52,36], 2) should return [5,6,52,36,12,10]
