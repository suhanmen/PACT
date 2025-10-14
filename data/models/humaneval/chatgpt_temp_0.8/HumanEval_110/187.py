def exchange(lst1, lst2):
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2, return "NO"
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Otherwise, perform the exchange and return "YES"
    else:
        for i in range(len(odd_nums)):
            lst1[lst1.index(odd_nums[i])] = even_nums[i]
        return "YES"
