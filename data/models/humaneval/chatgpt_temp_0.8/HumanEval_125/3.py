def split_words(txt):
    # Split the text on whitespace
    words = txt.split()
    
    # If there are no whitespace characters, split on commas
    if len(words) == 1:
        words = txt.split(',')
    
    # If there are still no words, count the number of lowercase letters with odd order in the alphabet
    if len(words) == 1:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
    
    return words
