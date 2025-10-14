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

    # Split the input string into sentences based on delimiters
    sentences = re.split("[.?!]", S)
    
    # Count the number of boredoms (sentences that start with "I")
    count = 0
    for sentence in sentences:
        if sentence.strip().startswith("I"):
            count += 1
    
    return count
