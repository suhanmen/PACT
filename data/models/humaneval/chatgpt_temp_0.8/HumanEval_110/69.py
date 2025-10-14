def exchange(lst1, lst2):
    # Find the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # Find the number of even elements in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    
    # If there are enough even elements in lst2 to replace the odd elements in lst1,
    # return "YES". Otherwise, return "NO".
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"
