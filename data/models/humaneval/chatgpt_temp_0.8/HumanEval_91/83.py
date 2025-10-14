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
    # Initialize the count of bored sentences to 0
    count = 0
    
    # Split the string into sentences
    sentences = re.split('[.?!]', S)
    
    # Check each sentence for the word "I" at the beginning
    for sentence in sentences:
        words = sentence.strip().split(' ')
        if len(words) > 0 and words[0] == 'I':
            count += 1
    
    return count
