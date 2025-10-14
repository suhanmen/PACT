"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""



def find_Max_Num(digits):
    # Convert integers to strings to concatenate them later
    str_digits = [str(digit) for digit in digits]
    
    # Sort the string digits in reverse order
    str_digits.sort(reverse=True)
    
    # Concatenate sorted string digits and convert to integer
    max_num = int(''.join(str_digits))
    return max_num

# Example usage
# assert find_Max_Num([1,2,3]) == 321
