def exchange(lst1, lst2):
    # Check if lst1 already contains all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and the even numbers in lst2
    odd_nums = [num for num in lst1 if num % 2 != 0]
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace the odd numbers in lst1, return "NO"
    if len(odd_nums) > len(even_nums):
        return "NO"
    
    # Sort both lists in ascending order
    odd_nums.sort()
    even_nums.sort()
    
    # Replace the odd numbers in lst1 with the even numbers from lst2
    for i in range(len(odd_nums)):
        lst1[lst1.index(odd_nums[i])] = even_nums[i]
        
    # Check if lst1 now contains all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
