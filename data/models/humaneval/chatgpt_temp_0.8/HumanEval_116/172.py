python
def sort_array(arr):
    # Create a lambda function to count the number of ones in the binary representation of a number
    count_ones = lambda x: bin(x).count('1')
    # Sort the array first by the number of ones, then by the decimal value
    arr.sort(key=lambda x: (count_ones(x), x))
    return arr
