def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = S.split('.')
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s != '']
    count = 0
    for s in sentences:
        if s.startswith('I'):
            count += 1
        else:
            sub_sentences = s.split('?')
            sub_sentences = [sub.strip() for sub in sub_sentences]
            sub_sentences = [sub for sub in sub_sentences if sub != '']
            for sub in sub_sentences:
                if sub.startswith('I'):
                    count += 1
                else:
                    sub_sub_sentences = sub.split('!')
                    sub_sub_sentences = [sub_sub.strip() for sub_sub in sub_sub_sentences]
                    sub_sub_sentences = [sub_sub for sub_sub in sub_sub_sentences if sub_sub != '']
                    for sub_sub in sub_sub_sentences:
                        if sub_sub.startswith('I'):
                            count += 1
    return count
