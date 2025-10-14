def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and the even numbers in lst2
    odd_nums = [num for num in lst1 if num % 2 != 0]
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # Check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(odd_nums) <= len(even_nums):
        return "YES"
    else:
        return "NO"
