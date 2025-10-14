def is_bored(S):
    count = 0
    sentences = S.split(".")
    for sentence in sentences:
        if sentence.strip().startswith("I"):
            count += 1
        elif "?" in sentence or "!" in sentence:
            sub_sentences = sentence.split("?") + sentence.split("!")
            for sub_sentence in sub_sentences:
                if sub_sentence.strip().startswith("I"):
                    count += 1
    return count
