"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""



def find_substring(string_list, substring):
    for string in string_list:
        if substring in string:
            return True
    return False

assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
