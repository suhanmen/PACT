def anti_shuffle(s):
    words = s.split()  # split string into words
    new_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))  # sort characters in word
        new_words.append(sorted_word)
    return ' '.join(new_words)  # join words back together with spaces
