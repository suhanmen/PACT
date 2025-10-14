def split_words(txt):
    # Split the text on whitespace, if possible
    words = txt.split()
    
    # If no whitespace exists, split on commas
    if len(words) == 1:
        words = txt.split(',')
    
    # If no commas exist, count the number of lowercase letters with odd alphabet order
    if len(words) == 1:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        return count
    
    # Otherwise, return the list of words
    return words
