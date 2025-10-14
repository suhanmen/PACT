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

    # Initialize variables
    boredom_count = 0
    sentences = S.split(".")
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]

    # Count the number of sentences starting with "I"
    for s in sentences:
        if s.startswith("I"):
            boredom_count += 1

    # Return the count of boredoms
    return boredom_count
