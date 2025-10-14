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
        if s.startswith("I "):
            count += 1
        elif s.startswith("I'"):
            count += 1
        elif s.startswith("I' "):
            count += 1
        elif s.startswith("I'm "):
            count += 1
        elif s.startswith("I am "):
            count += 1
        elif s.startswith("I'll "):
            count += 1
        elif s.startswith("I will "):
            count += 1
        elif s.startswith("I've "):
            count += 1
        elif s.startswith("I have "):
            count += 1
    return count
