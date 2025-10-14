def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if '?' in sentence:
            sub_sentences = sentence.split('?')
            for sub_sentence in sub_sentences:
                if '!' in sub_sentence:
                    sub_sub_sentences = sub_sentence.split('!')
                    for sub_sub_sentence in sub_sub_sentences:
                        if sub_sub_sentence.strip().startswith('I '):
                            count += 1
                elif sub_sentence.strip().startswith('I '):
                    count += 1
        elif '!' in sentence:
            sub_sentences = sentence.split('!')
            for sub_sentence in sub_sentences:
                if '?' in sub_sentence:
                    sub_sub_sentences = sub_sentence.split('?')
                    for sub_sub_sentence in sub_sub_sentences:
                        if sub_sub_sentence.strip().startswith('I '):
                            count += 1
                elif sub_sentence.
