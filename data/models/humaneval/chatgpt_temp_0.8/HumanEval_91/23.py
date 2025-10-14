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
    # initialize variables
    count = 0
    sentences = S.split(".")
    
    # check for "?" and "!" as well
    for sentence in sentences:
        words = sentence.split()
        if words and words[0] == "I":
            count += 1
        elif "?" in sentence:
            questions = sentence.split("?")
            for q in questions:
                words = q.split()
                if words and words[0] == "I":
                    count += 1
        elif "!" in sentence:
            exclamations = sentence.split("!")
            for ex in exclamations:
                words = ex.split()
                if words and words[0] == "I":
                    count += 1
                
    return count
