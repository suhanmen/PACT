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
    # initialize count to 0
    count = 0
    
    # split the string by '.', '?' or '!'
    sentences = S.split('. ') + S.split('? ') + S.split('! ')
    
    # loop through the sentences and check if they start with "I"
    for sentence in sentences:
        words = sentence.split()
        if words and words[0] == "I":
            count += 1
    
    return count
