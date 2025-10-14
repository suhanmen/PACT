"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""



def check(number):
    reverse_number = int(str(number)[::-1])
    return number == 2 * reverse_number - 1

# Example usage
# assert check(70) == False
