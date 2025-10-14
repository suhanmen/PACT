def exchange(lst1, lst2):
    # create a counter for the number of odd elements in lst1
    odd_count = 0
    
    # loop through lst1 and count the number of odd elements
    for num in lst1:
        if num % 2 != 0:  # if the number is odd
            odd_count += 1
    
    # if there are no odd elements in lst1, return "YES"
    if odd_count == 0:
        return "YES"
    
    # loop through lst2 and try to exchange elements with lst1
    for num in lst2:
        if num % 2 == 0:  # if the number is even
            lst1.append(num)  # add the number to lst1
            lst2.remove(num)  # remove the number from lst2
            
            # check if lst1 now contains only even elements
            odd_count = 0
            for num in lst1:
                if num % 2 != 0:  # if the number is odd
                    odd_count += 1
            if odd_count == 0:  # if there are no odd elements in lst1
                return "YES"
    
    return "NO"  # if no exchange was possible, return "NO"
