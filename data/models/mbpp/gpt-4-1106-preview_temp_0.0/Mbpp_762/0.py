"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""



def check_monthnumber_number(month_number):
    # List of months with 30 days
    months_with_30_days = [4, 6, 9, 11]
    return month_number in months_with_30_days

# Example usage:
# assert check_monthnumber_number(6) == True
