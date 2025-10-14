def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_uniq_count = 0
    max_uniq_word = ""
    for word in words:
        uniq_chars = set(word)
        uniq_count = len(uniq_chars)
        if uniq_count > max_uniq_count:
            max_uniq_count = uniq_count
            max_uniq_word = word
        elif uniq_count == max_uniq_count:
            max_uniq_word = min(max_uniq_word, word)
    return max_uniq_word
