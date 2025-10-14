"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""



def find_Odd_Pair(arr, n):
    odd_count = 0
    even_count = 0
    
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return odd_count * even_count

assert find_Odd_Pair([5,4,7,2,1],5) == 6
