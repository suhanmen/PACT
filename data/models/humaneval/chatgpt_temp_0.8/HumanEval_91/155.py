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
    
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if sentence:
            if sentence[0] == 'I':
                count += 1
            else:
                sentence = sentence.split('?')
                for s in sentence:
                    if s:
                        if s[0] == 'I':
                            count += 1
                        else:
                            s = s.split('!')
                            for ss in s:
                                if ss and ss[0] == 'I':
                                    count += 1
    return count
