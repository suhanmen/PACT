def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_len = -1
    max_word = ""
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > max_len:
            max_len = len(unique_chars)
            max_word = word
        elif len(unique_chars) == max_len:
            if word < max_word:
                max_word = word
    return max_word
