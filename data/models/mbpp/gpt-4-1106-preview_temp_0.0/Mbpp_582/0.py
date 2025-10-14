"""
Write a function to check if a dictionary is empty
assert my_dict({10})==False
"""



def my_dict(d):
    return not bool(d)

assert my_dict({}) == True
assert my_dict({10: None}) == False
