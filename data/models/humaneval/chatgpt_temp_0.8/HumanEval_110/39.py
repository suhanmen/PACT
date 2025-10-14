def exchange(lst1, lst2):
    even_nums = [num for num in lst1 if num % 2 == 0] # get all even numbers in lst1
    
    for num in lst2:
        if num % 2 == 0: # if num is even, try to exchange it with an odd number in lst1
            try:
                odd_idx = lst1.index([n for n in lst1 if n % 2 != 0][0]) # get index of first odd number in lst1
                lst1[odd_idx], lst2[lst2.index(num)] = lst2[lst2.index(num)], lst1[odd_idx] # exchange the numbers
            except IndexError: # if there are no odd numbers in lst1, don't make any exchanges
                pass
            
    if all(num % 2 == 0 for num in lst1): # if all numbers in lst1 are even, return "YES"
        return "YES"
    else: # if there are still odd numbers in lst1, return "NO"
        return "NO"
