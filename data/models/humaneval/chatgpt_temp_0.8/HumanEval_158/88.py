def find_max(words):
    max_word = ""
    max_count = 0

    for word in words:
        if len(set(word)) > max_count:
            max_word = word
            max_count = len(set(word))
        elif len(set(word)) == max_count:
            if word < max_word:
                max_word = word

    return max_word
