def exchange(lst1, lst2):
    # check if all elements of lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # create two lists of odd and even numbers from lst2
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    odd_lst2 = [num for num in lst2 if num % 2 != 0]
    
    # sort lst1 in ascending order
    lst1.sort()
    
    # iterate over lst1 and try to swap odd numbers with even numbers from lst2
    for i, num in enumerate(lst1):
        if num % 2 != 0:
            for j in range(len(even_lst2)):
                if even_lst2[j] < num:
                    lst1[i] = even_lst2[j]
                    even_lst2[j] = num
                    break
    
    # check if all elements of lst1 are now even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
