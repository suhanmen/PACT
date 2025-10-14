"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""



def toggle_string(s):
    return s.swapcase()

assert toggle_string("Python") == "pYTHON"
