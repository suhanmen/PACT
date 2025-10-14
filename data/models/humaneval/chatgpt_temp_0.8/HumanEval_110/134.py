def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0] # Create a list of even numbers in lst1
    odd_lst2 = [num for num in lst2 if num % 2 != 0] # Create a list of odd numbers in lst2
    
    if len(even_lst1) == len(lst1): # If lst1 is already all even, return "YES"
        return "YES"
    
    if len(even_lst1) > len(lst1) // 2: # If more than half of lst1 is already even, return "YES"
        return "YES"
    
    for num in odd_lst2: # For each odd number in lst2
        if num + sum(even_lst1) == sum(lst1) + num: # If swapping this number with some even number in lst1 can make lst1 all even
            return "YES"
    
    return "NO" # If we haven't found a way to make lst1 all even, return "NO"
