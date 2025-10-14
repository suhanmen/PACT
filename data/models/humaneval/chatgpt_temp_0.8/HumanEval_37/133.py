def sort_even(l: list):
    even_list = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    sorted_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            sorted_list.append(even_list.pop(0))
        else:
            sorted_list.append(l[i])
    return sorted_list
