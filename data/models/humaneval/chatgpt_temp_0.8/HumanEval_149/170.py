def sorted_list_sum(lst):
    # delete the strings that have odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # sort the list by ascending length of each word
    lst.sort(key=lambda word: (len(word), word))
    
    return lst
