def exchange(lst1, lst2):
    # check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # check if there are odd numbers in lst2 that can be exchanged
    for num in lst2:
        if num % 2 == 0:
            lst1.append(num)
            lst2.remove(num)
            if all(num % 2 == 0 for num in lst1):
                return "YES"

    # if no exchange was successful
    return "NO"
