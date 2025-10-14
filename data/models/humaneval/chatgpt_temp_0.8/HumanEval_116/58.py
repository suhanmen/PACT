python
def sort_array(arr):
    def count_ones(n):
        return bin(n).count('1') # count the number of 1s in the binary representation of n

    # sort the array using the count_ones function, and then by the actual value
    return sorted(arr, key=lambda x: (count_ones(x), x))
