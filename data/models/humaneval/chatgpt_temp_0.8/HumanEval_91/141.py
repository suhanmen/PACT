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

    # Split the input string into separate sentences
    sentences = re.split('[.?!]', S)

    # Initialize a counter for the number of boredoms
    boredom_count = 0

    # For each sentence, check if it starts with "I"
    for sentence in sentences:
        if sentence.strip().startswith("I"):
            boredom_count += 1

    return boredom_count
