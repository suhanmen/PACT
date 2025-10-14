def split_words(txt):
    # Split the text on whitespace
    words = txt.split()
    
    # If no whitespaces exist, split on commas
    if len(words) == 1:
        words = txt.split(",")
    
    # If no commas exist, count the number of lower-case letters with odd order in the alphabet
    if len(words) == 1:
        odd_count = 0
        for letter in txt.lower():
            if letter.isalpha() and ord(letter) % 2 == 1:
                odd_count += 1
        return odd_count
        
    return words
