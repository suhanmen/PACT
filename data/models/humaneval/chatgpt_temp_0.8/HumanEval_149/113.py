def sorted_list_sum(lst):
    # Creating an empty list to store only even length words
    even_len_words = []
    
    # Iterating over words in the input list
    for word in lst:
        if len(word) % 2 == 0: # Checking if the length of the word is even
            even_len_words.append(word) # Appending the even length word to the new list
    
    # Sorting the new list by length of each word and then alphabetically
    even_len_words.sort(key=lambda x: (len(x), x))
    
    return even_len_words
