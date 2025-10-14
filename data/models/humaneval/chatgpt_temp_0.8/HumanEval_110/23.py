def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count = sum([1 for num in lst1 if num % 2 != 0])
    
    # If there are no odd numbers in lst1, return "YES"
    if odd_count == 0:
        return "YES"
    
    # Iterate over the elements in lst2
    for num in lst2:
        # If the element is even and lst1 still has odd numbers
        if num % 2 == 0 and odd_count > 0:
            # Decrement the odd_count and continue iterating
            odd_count -= 1
            continue
        
        # If the element is odd and lst1 has odd numbers
        if num % 2 != 0 and odd_count > 0:
            # Swap the odd element in lst1 with the even element in lst2
            for i in range(len(lst1)):
                if lst1[i] % 2 != 0 and lst2[i] % 2 == 0:
                    lst1[i], lst2[i] = lst2[i], lst1[i]
                    odd_count -= 1
                    break
                    
    # Check if lst1 now only contains even numbers
    if sum([1 for num in lst1 if num % 2 
