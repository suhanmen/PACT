"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""



def reverse_words(s):
    return ' '.join(reversed(s.split()))

assert reverse_words("python program") == ("program python")
