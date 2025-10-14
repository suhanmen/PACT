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
    # Initialize a counter for the number of boredoms
    num_boredoms = 0
    
    # Split the string into sentences
    sentences = S.split(".")
    sentences += S.split("?")
    sentences += S.split("!")
    
    # Loop through each sentence and check if it starts with "I"
    for sentence in sentences:
        if sentence.strip().startswith("I"):
            num_boredoms += 1
    
    return num_boredoms
