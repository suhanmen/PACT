def exchange(lst1, lst2):
    # check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # get the indices of the even numbers in lst1
    even_indices = [i for i, num in enumerate(lst1) if num % 2 == 0]

    # check if there are any even numbers in lst1
    if not even_indices:
        return "NO"

    # check if there are any odd numbers in lst2
    if any(num % 2 != 0 for num in lst2):
        return "NO"

    # exchange the even numbers in lst1 with the odd numbers in lst2
    for i in even_indices:
        for j, num in enumerate(lst2):
            if num % 2 != 0:
                lst1[i], lst2[j] = lst2[j], lst1[i]
                break

    # check if all elements in lst1 are even after the exchange
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
