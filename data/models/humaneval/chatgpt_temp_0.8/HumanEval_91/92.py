def is_bored(S):
    count = 0
    sentences = S.split(".")
    for sentence in sentences:
        if sentence.startswith("I"):
            count += 1
        else:
            sentences2 = sentence.split("?")
            for sentence2 in sentences2:
                if sentence2.startswith("I"):
                    count += 1
                else:
                    sentences3 = sentence2.split("!")
                    for sentence3 in sentences3:
                        if sentence3.startswith("I"):
                            count += 1
    return count
