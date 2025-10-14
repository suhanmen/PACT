def total_match(lst1, lst2):
    lst1_chars = sum(len(word) for word in lst1)
    lst2_chars = sum(len(word) for word in lst2)

    if lst1_chars < lst2_chars:
        return lst1
    elif lst1_chars > lst2_chars:
        return lst2
    else:
        return lst1
