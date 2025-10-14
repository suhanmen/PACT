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
    boredoms = 0
    sentences = S.split('.')
    for sentence in sentences:
        if sentence.startswith("I"):
            boredoms += 1
        else:
            sub_sentences = sentence.split('?')
            for sub_sentence in sub_sentences:
                if sub_sentence.startswith("I"):
                    boredoms += 1
                else:
                    sub_sub_sentences = sub_sentence.split('!')
                    for sub_sub_sentence in sub_sub_sentences:
                        if sub_sub_sentence.startswith("I"):
                            boredoms += 1
    return boredoms
