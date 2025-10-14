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

    # split the string into sentences
    sentences = S.split(".")
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s != ""]

    # add sentences that end with '?' or '!'
    continued_sentence = ""
    for sentence in sentences:
        if sentence[-1] in ['?', '!']:
            continued_sentence += sentence
            if continued_sentence:
                continued_sentence = continued_sentence.strip()
                if continued_sentence.startswith("I "):
                    return 1
            continued_sentence = ""
        else:
            continued_sentence += sentence + " "

    # check if the last sentence starts with "I"
    if continued_sentence and continued_sentence.startswith("I "):
        return 1

    # no boredoms found
    return 0
