def anti_shuffle(s):
    new_s = ''
    for word in s.split():
        sorted_word = ''.join(sorted(word))
        new_s += sorted_word + ' '
    return new_s[:-1]
