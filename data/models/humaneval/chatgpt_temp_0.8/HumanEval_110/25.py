def exchange(lst1, lst2):
    # count the number of odd numbers in lst1
    odd_count = sum(1 for x in lst1 if x % 2 == 1)
    # check if it is possible to exchange elements to make lst1 all even
    if odd_count <= len(lst2):
        return "YES"
    else:
        return "NO"
