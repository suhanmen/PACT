def anti_shuffle(s):
    words = s.split(' ')
    new_sentence = ''
    for word in words:
        sorted_word = ''.join(sorted(word))
        new_sentence += sorted_word + ' '
    return new_sentence[:-1]  # remove the trailing space
