def anti_shuffle(s):
    words = s.split(' ')
    new_sentence = ''
    for word in words:
        new_word = ''.join(sorted(word, key=lambda x: ord(x)))
        new_sentence += new_word + ' '
    return new_sentence.strip()
