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
    if ' ' in txt:
        # if whitespace exists, split on whitespace
        return txt.split()
    elif ',' in txt:
        # if no whitespace but commas exist, split on commas
        return txt.split(',')
    else:
        # count number of lower-case letters with odd order
        count = 0
        for i in txt:
            if i.islower():
                if ord(i) % 2 == 1:
                    count += 1
        return count
