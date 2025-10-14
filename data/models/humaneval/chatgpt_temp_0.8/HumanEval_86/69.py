def anti_shuffle(s):
    words = s.split()
    result = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        result.append(sorted_word)
    return ' '.join(result)
