def exchange(lst1, lst2):
    # Find the sum of odd numbers in lst1
    odd_sum = sum([num for num in lst1 if num % 2 != 0])
    
    # Find the number of even numbers in lst2
    even_count = len([num for num in lst2 if num % 2 == 0])
    
    # If there are enough even numbers in lst2 to replace the odd numbers in lst1, return "YES"
    if even_count >= (odd_sum + 1) // 2:
        return "YES"
    else:
        return "NO"
