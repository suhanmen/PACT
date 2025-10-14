def sorted_list_sum(lst):
    #create an empty list to store the even-length words
    even_lst = []
    
    #iterate through the words and add even-length words to the even_lst
    for word in lst:
        if len(word) % 2 == 0:
            even_lst.append(word)

    #sort the even-length words first by length and then alphabetically
    even_lst.sort(key=lambda x: (len(x), x))

    return even_lst
