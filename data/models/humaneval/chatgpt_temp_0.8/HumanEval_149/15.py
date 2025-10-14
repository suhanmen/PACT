def sorted_list_sum(lst):
    # Creating a new list that only contains strings with even length
    even_length_lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sorting the even-length list first by length and then alphabetically
    sorted_lst = sorted(even_length_lst, key=lambda x: (len(x), x))
    
    return sorted_lst
