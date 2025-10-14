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
    
    # Split the input string into sentences based on delimiters
    sentences = S.split(".")
    for sentence in sentences:
        # Check if the sentence starts with "I"
        if sentence.strip().startswith("I"):
            num_boredoms += 1
        
        # Split the sentence again based on question marks and exclamation points
        sub_sentences = sentence.split("?") + sentence.split("!")
        for sub_sentence in sub_sentences:
            # Check if the sub-sentence starts with "I"
            if sub_sentence.strip().startswith("I"):
                num_boredoms += 1
    
    # Return the final count of boredoms
    return num_boredoms
