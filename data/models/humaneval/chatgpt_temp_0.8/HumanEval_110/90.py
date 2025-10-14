def exchange(lst1, lst2):
    # Check if lst1 already has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if there are odd numbers in lst2 that can be exchanged with even numbers in lst1
    for num in lst2:
        if num % 2 == 0 and (num/2) in lst1:
            return "YES"
    
    # If we haven't returned by now, it's not possible to make lst1 all even
    return "NO"
