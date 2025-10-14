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
    for s in sentences:
        if "?" in s:
            s = s.split("?")
            for sub_s in s:
                if "!" in sub_s:
                    sub_s = sub_s.split("!")
                    for sub_sub_s in sub_s:
                        if sub_sub_s.strip().startswith("I "):
                            count += 1
                elif sub_s.strip().startswith("I "):
                    count += 1
        elif "!" in s:
            s = s.split("!")
            for sub_s in s:
                if "?" in sub_s:
                    sub_s = sub_s.split("?")
                    for sub_sub_s in sub_s:
                        if sub_sub_s.strip().startswith("I "):
                            count += 1
                elif sub_s.strip().startswith("I "):
                    count += 1
        elif s.strip().startswith("I "):
            count += 1
            
    return count
