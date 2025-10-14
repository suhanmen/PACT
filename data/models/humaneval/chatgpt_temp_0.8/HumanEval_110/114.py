def exchange(lst1, lst2):
    # check if lst1 already consists of only even numbers
    if all(x % 2 == 0 for x in lst1):
        return "YES"

    # calculate the number of odd elements in lst1
    odd_count = sum(1 for x in lst1 if x % 2 == 1)

    # calculate the number of even elements in lst2
    even_count = sum(1 for x in lst2 if x % 2 == 0)

    # check if there are enough even elements in lst2 to replace the odd elements in lst1
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"
