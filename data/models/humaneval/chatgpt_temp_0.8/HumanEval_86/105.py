def anti_shuffle(s):
    result = []
    for word in s.split():
        sorted_word = ''.join(sorted(word))
        result.append(sorted_word)
    return ' '.join(result)
