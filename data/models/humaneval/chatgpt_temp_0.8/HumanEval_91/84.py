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
        if sentence.startswith('I'):
            count += 1
        else:
            questions = sentence.split('?')
            for question in questions:
                if question.startswith('I'):
                    count += 1
                else:
                    exclaims = question.split('!')
                    for exclaim in exclaims:
                        if exclaim.startswith('I'):
                            count += 1
    return count
