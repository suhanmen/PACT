def select_words(s, n):
    consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    words = s.split()
    selected_words = []
    for word in words:
        if len(word) == 0:
            continue
        num_consonants = 0
        for letter in word:
            if letter.lower() in consonants:
                num_consonants += 1
        if num_consonants == n:
            selected_words.append(word)
    return selected_words
