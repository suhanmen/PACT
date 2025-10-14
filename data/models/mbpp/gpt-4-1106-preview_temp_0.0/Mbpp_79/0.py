"""
Write a python function to check whether the length of the word is odd or not.
assert word_len("Hadoop") == False
"""



def word_len(word):
    return len(word) % 2 != 0

assert word_len("Hadoop") == False
