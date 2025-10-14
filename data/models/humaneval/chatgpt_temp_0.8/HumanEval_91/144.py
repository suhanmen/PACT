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
    count = 0
    sentences = S.split(".")
    for sentence in sentences:
        if "?" in sentence:
            sub_sentences = sentence.split("?")
            for sub_sentence in sub_sentences:
                if "!" in sub_sentence:
                    mini_sentences = sub_sentence.split("!")
                    for mini_sentence in mini_sentences:
                        if mini_sentence.startswith("I"):
                            count += 1
                else:
                    if sub_sentence.startswith("I"):
                        count += 1
        elif "!" in sentence:
            sub_sentences = sentence.split("!")
            for sub_sentence in sub_sentences:
                if "?" in sub_sentence:
                    mini_sentences = sub_sentence.split("?")
                    for mini_sentence in mini_sentences:
                        if mini_sentence.startswith("I"):
                            count += 1
                else:
                    if sub_sentence
