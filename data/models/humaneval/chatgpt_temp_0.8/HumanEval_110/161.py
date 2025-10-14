def exchange(lst1, lst2):
    # create a set of indices of odd numbers in lst1
    odds = set(i for i in range(len(lst1)) if lst1[i] % 2 == 1)
    
    # create a set of indices of even numbers in lst2
    evens = set(i for i in range(len(lst2)) if lst2[i] % 2 == 0)
    
    # if there are enough even numbers in lst2 to replace all the odd numbers in lst1, return "YES"
    if len(evens) >= len(odds):
        return "YES"
    else:
        return "NO"
