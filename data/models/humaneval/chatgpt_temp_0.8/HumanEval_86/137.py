def anti_shuffle(s):
    # Split the input string into a list of words
    words = s.split()

    # For each word, sort its characters by ascii value
    ordered_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        ordered_words.append(sorted_word)

    # Combine the ordered words into a single string, preserving spaces
    ordered_s = ''
    for i, word in enumerate(ordered_words):
        ordered_s += word
        if i < len(words) - 1:
            ordered_s += ' '

    return ordered_s
