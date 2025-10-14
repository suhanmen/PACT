def anti_shuffle(s):
    new_s = []
    for word in s.split():
        new_word = ''.join(sorted(word))
        new_s.append(new_word)
    return ' '.join(new_s)
