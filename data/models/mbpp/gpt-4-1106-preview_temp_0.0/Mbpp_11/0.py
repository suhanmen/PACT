"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""



def remove_Occ(string, char):
    first_occ = string.find(char)
    if first_occ != -1:
        string = string[:first_occ] + string[first_occ+1:]
    last_occ = string.rfind(char)
    if last_occ != -1:
        string = string[:last_occ] + string[last_occ+1:]
    return string

assert remove_Occ("hello","l") == "heo"
