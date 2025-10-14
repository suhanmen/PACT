def split_words(txt):
    # Split the text by whitespace
    words = txt.split()
    
    # If there are no whitespace characters, split by comma
    if len(words) == 1:
        words = txt.split(",")
        
    # If there are still no commas, count lowercase letters with odd order in the alphabet
    if len(words) == 1:
        count = sum(1 for c in txt if c.islower() and ord(c) % 2 != 0)
        return count
        
    return words
