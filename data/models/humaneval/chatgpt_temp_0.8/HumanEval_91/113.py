def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if '?' in sentence:
            sentences += sentence.split('?')
        elif '!' in sentence:
            sentences += sentence.split('!')
        else:
            if sentence.startswith('I'):
                count += 1
    return count
