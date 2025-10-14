def anti_shuffle(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))
    return ' '.join(words)
