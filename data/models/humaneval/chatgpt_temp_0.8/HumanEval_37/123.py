def sort_even(l: list):
    even = sorted([l[i] for i in range(0, len(l), 2)])
    new_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            new_list.append(l[i])
        else:
            new_list.append(even.pop(0))
    return new_list
