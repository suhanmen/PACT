def is_bored(S):
    sentences = S.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    sentences.extend([s.strip() for s in S.split('?') if s.strip()])
    sentences.extend([s.strip() for s in S.split('!') if s.strip()])
    
    count = 0
    for s in sentences:
        words = s.split()
        if words and words[0].lower() == 'i':
            count += 1
    
    return count
