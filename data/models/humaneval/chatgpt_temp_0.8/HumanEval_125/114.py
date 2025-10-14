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

    # Check if there are whitespaces in the text, split on whitespace if true
    if ' ' in txt:
        words = txt.split()
        return words

    # Check if there are commas in the text, split on commas if true
    elif ',' in txt:
        words = txt.split(',')
        return words

    # Count the number of lower-case letters with odd order in the alphabet
    else:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        return count
