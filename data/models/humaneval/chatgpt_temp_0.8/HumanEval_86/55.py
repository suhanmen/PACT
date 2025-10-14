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

    # Split the string into individual words
    words = s.split()

    # Create a list to store the ordered versions of each word
    ordered_words = []

    # Loop through each word in the list
    for word in words:

        # Convert the word to a list of characters
        chars = list(word)

        # Sort the list of characters in ascending order based on ascii value
        chars.sort()

        # Join the sorted characters back into a word
        ordered_word = ''.join(chars)

        # Add the ordered word to the list of ordered words
        ordered_words.append(ordered_word)

    # Join the ordered words back into a string, keeping the original order of words and spaces
    ordered_string = ' '.join(ordered_words)

    return ordered_string
