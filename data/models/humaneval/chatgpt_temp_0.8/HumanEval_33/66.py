def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    """
    div_by_three = []
    not_div_by_three = []
    for i in range(len(l)):
        if i % 3 == 0:
            div_by_three.append(l[i])
        else:
            not_div_by_three.append(l[i])
    div_by_three.sort()
    new_list = []
    j = 0
    k = 0
    for i in range(len(l)):
        if i % 3 == 0:
            new_list.append(div_by_three[j])
            j += 1
        else:
            new_list.append(not_div_by_three[k])
            k += 1
    return new_list
