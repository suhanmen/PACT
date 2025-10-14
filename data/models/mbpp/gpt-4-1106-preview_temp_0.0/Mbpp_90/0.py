"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""



def len_log(words):
    return max(len(word) for word in words)

assert len_log(["python","PHP","bigdata"]) == 7
