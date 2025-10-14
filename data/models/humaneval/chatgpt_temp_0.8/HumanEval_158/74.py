def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """

    max_unique_chars = 0
    word_with_max_unique_chars = ""

    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_unique_chars:
            max_unique_chars = len(unique_chars)
            word_with_max_unique_chars = word
        elif len(unique_chars) == max_unique_chars:
            if word < word_with_max_unique_chars:
                word_with_max_unique_chars = word

    return word_with_max_unique_chars
