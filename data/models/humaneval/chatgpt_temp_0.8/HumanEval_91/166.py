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
    sentences = [s for s in sentences if s]
    
    count = 0
    for s in sentences:
        if s.startswith('I'):
            count += 1
        else:
            s = s.split('?')
            s = [ss.strip() for ss in s]
            s = [ss for ss in s if ss]
            for ss in s:
                if ss.startswith('I'):
                    count += 1
                else:
                    ss = ss.split('!')
                    ss = [sss.strip() for sss in ss]
                    ss = [sss for sss in ss if sss]
                    for sss in ss:
                        if sss.startswith('I'):
                            count += 1
    
    return count
