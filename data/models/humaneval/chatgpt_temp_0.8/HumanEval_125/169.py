python
def split_words(txt):
    words = txt.split()
    
    # If there are no spaces in the text, split on commas
    if len(words) == 1:
        words = txt.split(',')
    
    # If there are still no words, count the number of lowercase letters with odd order 
    if len(words) == 1:
        count = sum(1 for letter in txt if letter.islower() and ord(letter) % 2 == 1)
        return count
    
    return words
