def sorted_list_sum(lst):
    # filtering out strings with odd length from list 'lst'
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # sorting the filtered list based on length and alphabetically
    lst.sort(key=lambda word: (len(word), word))
    
    return lst
