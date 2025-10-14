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
    sentences = [sentence.strip() for sentence in sentences]
    sentences = [sentence for sentence in sentences if sentence]
    
    count = 0
    for sentence in sentences:
        if sentence.startswith("I"):
            count += 1
        elif '?' in sentence or '!' in sentence:
            if sentence.split('?')[0].startswith("I") or sentence.split('!')[0].startswith("I"):
                count += 1
    
    return count
