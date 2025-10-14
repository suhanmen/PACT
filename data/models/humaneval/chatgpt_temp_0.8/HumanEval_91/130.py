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
    # Initialize the boredom count to 0
    boredom_count = 0
    
    # Split the string into sentences
    sentences = S.split('.')
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.strip().startswith("I"):
            boredom_count += 1
            continue
        sentences = sentence.split('?')
        for sentence in sentences:
            # Check if the sentence starts with "I"
            if sentence.strip().startswith("I"):
                boredom_count += 1
                continue
            sentences = sentence.split('!')
            for sentence in sentences:
                # Check if the sentence starts with "I"
                if sentence.strip().startswith("I"):
                    boredom_count += 1
    
    return boredom_count
