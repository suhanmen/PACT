"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""



def check_monthnumb_number(month_number):
    # List of month numbers with 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    return month_number in months_with_31_days

# Example usage:
# assert check_monthnumb_number(5) == True
