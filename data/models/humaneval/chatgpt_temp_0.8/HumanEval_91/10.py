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
    # Initialize a counter variable to keep track of the number of boredoms
    boredom_count = 0

    # Split the string into sentences using the delimiters ('.', '?', '!')
    sentences = S.split(".")
    for sentence in sentences:
        if "?" in sentence:
            sub_sentences = sentence.split("?")
            for sub_sentence in sub_sentences:
                if "!" in sub_sentence:
                    sub_sub_sentences = sub_sentence.split("!")
                    for sub_sub_sentence in sub_sub_sentences:
                        if "I " in sub_sub_sentence.strip().split(" ")[0]:
                            boredom_count += 1
                elif "I " in sub_sentence.strip().split(" ")[0]:
                    boredom_count += 1
        elif "!" in sentence:
            sub_sentences = sentence.split("!")
            for sub_sentence in sub_sentences:
                if "?" in sub_sentence:
                    sub_sub_sentences = sub_sentence.split("?")
                    
