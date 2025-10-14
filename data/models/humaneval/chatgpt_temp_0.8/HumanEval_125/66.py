def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''

    # Check if the text contains whitespaces
    if " " in txt:
        # Split the text on whitespaces and return the resulting list
        return txt.split()
    
    # Check if the text contains commas
    elif "," in txt:
        # Split the text on commas and return the resulting list
        return txt.split(",")
    
    else:
        # Count the number of lowercase letters with odd order in the alphabet
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        # Return the count
        return count
