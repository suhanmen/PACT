"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""



def long_words(n, sentence):
    words = sentence.split()
    return [word for word in words if len(word) > n]

assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
