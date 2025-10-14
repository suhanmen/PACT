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
    # Initialize boredom count to 0
    boredom_count = 0
    
    # Split the string into sentences using '.', '?' or '!' as delimiters
    sentences = re.split('[.?!]', S)
    
    # Loop through each sentence and check if it starts with "I"
    for sentence in sentences:
        # Strip leading and trailing whitespace from the sentence
        sentence = sentence.strip()
        if sentence.startswith("I"):
            boredom_count += 1
    
    # Return the boredom count
    return boredom_count
