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
    # initialize boredom count
    boredom_count = 0
    
    # split the string into sentences
    sentences = re.split('[.?!]', S)
    
    # iterate through the sentences
    for sentence in sentences:
        # clean up the sentence
        sentence = sentence.strip()
        if len(sentence) > 0:
            # check if the sentence starts with "I"
            if sentence[0] == "I":
                boredom_count += 1
    
    # return the boredom count
    return boredom_count
