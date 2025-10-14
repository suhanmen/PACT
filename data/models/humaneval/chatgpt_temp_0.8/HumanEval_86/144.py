def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split() # split the string into words
    sorted_words = []
    for word in words:
        sorted_word = ''.join(sorted(word)) # sort the characters in the word based on ascii value
        sorted_words.append(sorted_word)
    # combine the sorted words back into a string with spaces in between
    return ' '.join(sorted_words)
