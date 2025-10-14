def anti_shuffle(s):
    words = s.split() # split the string into a list of words
    ordered_words = [] # initialize empty list to hold ordered words
    for word in words: # loop through each word
        ordered_word = ''.join(sorted(word)) # sort the characters in the word and join them back together
        ordered_words.append(ordered_word) # add the ordered word to the list
    return ' '.join(ordered_words) # join the ordered words back into a string, separated by spaces
