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
    
    # Initialize boredom counter to zero
    boredom_counter = 0

    # Split the string into sentences
    sentences = S.split(".")
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s]

    sentences = [s.split("?") for s in sentences]
    sentences = [sentence for sublist in sentences for sentence in sublist]
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s]

    sentences = [s.split("!") for s in sentences]
    sentences = [sentence for sublist in sentences for sentence in sublist]
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s]

    # Check if each sentence starts with "I"
    for sentence in sentences:
        if sentence.startswith("I"):
            boredom_counter += 1

    return boredom_counter
