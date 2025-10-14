def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    
    words = s.split() # split the string into words
    ordered_words = [] # list to hold ordered words
    
    for word in words:
        ordered_word = ''.join(sorted(word)) # sort the characters in the word
        ordered_words.append(ordered_word) # add the sorted word to the list
    
    # combine the ordered words with the original spaces
    result = ''
    for i in range(len(words)):
        result += ordered_words[i]
        if i < len(words) - 1:
            result += ' ' # add a space if not at the end of the sentence
    
    return result
