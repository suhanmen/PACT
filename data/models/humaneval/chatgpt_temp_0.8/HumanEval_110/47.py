def exchange(lst1, lst2):
    # Counting the number of odd numbers in lst1
    odd_count = sum([1 for num in lst1 if num % 2 != 0])
    
    # If odd_count is zero, lst1 already contains all even numbers
    if odd_count == 0:
        return "YES"
    
    # Checking if it's possible to exchange odd numbers in lst1 with even numbers in lst2
    for num in lst2:
        if num % 2 == 0:
            lst1.append(num)
            odd_count -= 1
            if odd_count == 0:
                return "YES"
    
    return "NO"
