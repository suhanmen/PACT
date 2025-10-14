def anti_shuffle(s):
    words_list = s.split()
    ordered_words_list = []

    for word in words_list:
        ordered_word = ''.join(sorted(word))
        ordered_words_list.append(ordered_word)
        
    return ' '.join(ordered_words_list)
