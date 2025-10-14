def exchange(lst1, lst2):
    # find the odd elements in lst1 and the even elements in lst2
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    
    # check if length of odd_lst1 is greater than length of even_lst2
    if len(odd_lst1) > len(even_lst2):
        return "NO"
    else:
        return "YES"
