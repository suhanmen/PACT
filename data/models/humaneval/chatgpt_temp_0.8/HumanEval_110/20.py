def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the even numbers in lst2 that can be exchanged with odd numbers in lst1
    even_nums = [num for num in lst2 if num % 2 == 0 and num not in lst1]
    odd_nums = [num for num in lst1 if num % 2 == 1]
    
    # If there are not enough even numbers in lst2 to make lst1 all even, return "NO"
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Swap the odd numbers in lst1 with even numbers in lst2 until lst1 contains only even numbers
    for i in range(len(odd_nums)):
        lst1[lst1.index(odd_nums[i])] = even_nums[i]
    
    return "YES"
