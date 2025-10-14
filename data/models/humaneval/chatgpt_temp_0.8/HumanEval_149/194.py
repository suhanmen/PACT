def sorted_list_sum(lst):
    # Create a new list containing only strings with even lengths
    new_list = [string for string in lst if len(string) % 2 == 0]
    
    # Sort the new list by length, then alphabetically
    new_list.sort(key=lambda x: (len(x), x))
    
    return new_list
