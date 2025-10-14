def exchange(lst1, lst2):
    # Check if lst1 contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and the even numbers in lst2
    odd_nums = [num for num in lst1 if num % 2 != 0]
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2, return "NO"
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Exchange the odd numbers in lst1 with even numbers in lst2
    for i in range(len(odd_nums)):
        lst1[lst1.index(odd_nums[i])] = even_nums[i]
    
    # Check if lst1 contains only even numbers after the exchange
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
