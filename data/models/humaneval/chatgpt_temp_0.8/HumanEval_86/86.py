def anti_shuffle(s):
    words = s.split()  # split the string into words
    ordered_words = []
    
    # loop through the words and order them
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)
    
    return ' '.join(ordered_words)
