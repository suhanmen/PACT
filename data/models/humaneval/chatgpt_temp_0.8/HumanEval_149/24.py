def sorted_list_sum(lst):
    lst = [i for i in lst if len(i)%2 == 0] # Removing odd length strings
    lst.sort(key=lambda x: (len(x), x)) # Sorting the list by length and lexicographically
    return lst
