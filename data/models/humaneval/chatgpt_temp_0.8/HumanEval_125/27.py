def split_words(txt):
    # Split the text on whitespace
    words = txt.split()
    
    # If no whitespace, split on commas
    if len(words) == 1 and "," in words[0]:
        words = words[0].split(",")
    
    # If still no words, count number of lowercase letters with odd order
    if len(words) == 1:
        count = 0
        for char in words[0]:
            if char.islower() and ord(char) % 2 == 1:
                count += 1
        return count
    
    return words
