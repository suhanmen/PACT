def find_max(words):
    """
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """

    def count_unique_chars(word):
        """
        A helper function that returns the count of unique characters in a word.
        """
        return len(set(word))

    # Sort the list of words in lexicographical order
    words = sorted(words)

    # Initialize variables to keep track of the word with maximum number of unique characters
    max_word = ""
    max_count = 0

    # Iterate through each word in the list
    for word in words:
        # Get the count of unique characters in the current word
        count = count_unique_chars(wo
