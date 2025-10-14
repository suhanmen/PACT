def is_bored(S):
    boredom_count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if '?' in sentence:
            sub_sentences = sentence.split('?')
            for sub_sentence in sub_sentences:
                if '!' in sub_sentence:
                    sub_sub_sentences = sub_sentence.split('!')
                else:
                    sub_sub_sentences = [sub_sentence]
        elif '!' in sentence:
            sub_sentences = sentence.split('!')
            for sub_sentence in sub_sentences:
                if '?' in sub_sentence:
                    sub_sub_sentences = sub_sentence.split('?')
                else:
                    sub_sub_sentences = [sub_sentence]
        else:
            sub_sub_sentences = [sentence]
        for sub_sub_sentence in sub_sub_sentences:
            if sub_sub_sentence.strip().startswith('I '):
                boredom_count += 1
    return boredom_count
