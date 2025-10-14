def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if there are odd numbers in lst2 that can be exchanged with even numbers in lst1
    for num in lst2:
        if num % 2 == 0 and any(n % 2 == 1 for n in lst1):
            lst1[lst1.index(next(n for n in lst1 if n % 2 == 1))] = num
            if all(n % 2 == 0 for n in lst1):
                return "YES"
    
    return "NO"
