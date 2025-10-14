def is_bored(S):
    count = 0
    sentences = S.split(".")
    for sentence in sentences:
        if "?" in sentence:
            subsentences = sentence.split("?")
            for subsentence in subsentences:
                if "!" in subsentence:
                    subsubsentences = subsentence.split("!")
                    for subsubsentence in subsubsentences:
                        if subsubsentence.strip().startswith("I"):
                            count += 1
                elif subsentence.strip().startswith("I"):
                    count += 1
        elif "!" in sentence:
            subsentences = sentence.split("!")
            for subsentence in subsentences:
                if "?" in subsentence:
                    subsubsentences = subsentence.split("?")
                    for subsubsentence in subsubsentences:
                        if subsubsentence.strip().startswith("I"):
                            count += 1
                elif subsentence.strip().startswith("I"):
      
