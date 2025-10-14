def anti_shuffle(s):
    words = s.split() # separate the words in the string
    new_words = [] # create an empty list to hold the new words
    for word in words:
        sorted_word = "".join(sorted(word)) # sort the characters in the word
        new_words.append(sorted_word) # add the sorted word to the list
    return " ".join(new_words) # join the new words together and return the result
