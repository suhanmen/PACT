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
    bored_count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if sentence.strip().startswith("I"):
            bored_count += 1
        else:
            for char in ['?', '!']:
                if char in sentence:
                    subsentences = sentence.split(char)
                    for subsentence in subsentences:
                        if subsentence.strip().startswith("I"):
                            bored_count += 1
                            break
                    break
    return bored_count
