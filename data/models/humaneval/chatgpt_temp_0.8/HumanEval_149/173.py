def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0]  # Remove words with odd lengths
    lst.sort(key=lambda x: (len(x), x))  # Sort by ascending length and alphabetical order
    return lst
