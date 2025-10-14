def exchange(lst1, lst2):
    # check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # find all even numbers in lst2
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    
    # find all odd numbers in lst1
    odd_lst1 = [num for num in lst1 if num % 2 == 1]
    
    # if there are not enough even numbers in lst2 to replace all odd numbers in lst1, return "NO"
    if len(even_lst2) < len(odd_lst1):
        return "NO"
    
    # perform the exchange of elements between lst1 and lst2
    for i in range(len(lst1)):
        if lst1[i] % 2 == 1:  # if the element in lst1 is odd
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:  # if the element in lst2 is even
                    lst1[i], lst2[j] = lst2[j], lst1[i]  # exchange the elements
                    break  # move on to the next element in lst1
        
        # check if lst1 now contains only even numbers
        if all(num % 2 == 0 for num in lst1):
     
