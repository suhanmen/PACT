def sort_array(arr):
    def count_ones(num):
        # count number of ones in binary representation of num
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count
    
    # sort arr based on number of ones and decimal value
    return sorted(arr, key=lambda x: (count_ones(x), x))
