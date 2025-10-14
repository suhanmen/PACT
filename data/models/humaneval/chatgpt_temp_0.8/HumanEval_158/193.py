def find_max(words):
    max_num_unique_chars = -1
    result_word = ""

    for word in words:
        num_unique_chars = len(set(word))

        if num_unique_chars > max_num_unique_chars:
            max_num_unique_chars = num_unique_chars
            result_word = word

        elif num_unique_chars == max_num_unique_chars:
            if word < result_word:
                result_word = word

    return result_word
