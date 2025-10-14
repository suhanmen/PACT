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
    # Split the string into sentences based on '.', '?' or '!'
    sentences = re.split('[.?!]', S)
    
    boredom_count = 0
    
    # Iterate over each sentence and check if it starts with 'I'
    for sentence in sentences:
        words = sentence.strip().split()
        if words and words[0].lower() == 'i':
            boredom_count += 1
    
    return boredom_count
