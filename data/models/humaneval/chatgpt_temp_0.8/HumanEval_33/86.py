def sort_third(l: list):
    new_list = l.copy()
    third_indices = [i for i in range(len(l)) if i % 3 == 0]
    for index in third_indices:
        sublist = l[index:index+3]
        sorted_sublist = sorted(sublist)
        new_list[index:index+3] = sorted_sublist
    return new_list
