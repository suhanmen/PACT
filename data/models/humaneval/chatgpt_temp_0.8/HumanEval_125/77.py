def split_words(txt):
    words = txt.split()
    
    if len(words) == 1 and ',' in txt:
        words = txt.split(',')
        
    if len(words) == 1:
        odd_count = sum([1 for c in txt if c.islower() and ord(c)%2==1])
        return odd_count
        
    return words
