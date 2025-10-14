def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    new_lst = [word for word in lst if len(word)%2 == 0]
    
    # Sort the list by length of each word (ascending)
    # If two words have the same length, sort alphabetically
    new_lst.sort(key=lambda word: (len(word), word))
    
    return new_lst
