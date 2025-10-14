def sorted_list_sum(lst):
    # Remove strings with odd length
    lst = [string for string in lst if len(string) % 2 == 0]
    # Sort by length and then alphabetically
    lst = sorted(lst, key=lambda string: (len(string), string))
    return lst
