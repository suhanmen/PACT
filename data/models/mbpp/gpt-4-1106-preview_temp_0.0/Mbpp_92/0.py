"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""



def is_undulating(number):
    str_num = str(number)
    if len(str_num) < 3 or len(set(str_num)) != 2:
        return False
    return all(str_num[i] != str_num[i+1] for i in range(len(str_num) - 1))

# Example usage:
# print(is_undulating(1212121))  # Output: True
