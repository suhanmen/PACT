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

    # Split the string into words
    words = s.split()

    # Initialize an empty list to store the ordered words
    ordered_words = []

    # Loop through each word in the list, sort the characters in the word,
    # and add the sorted word to the ordered_words list
    for word in words:
        sorted_word = ''.join(sorted(word))
        ordered_words.append(sorted_word)

    # Join the ordered_words list into a string, using spaces to separate the words
    ordered_string = ' '.join(ordered_words)

    return ordered_string
