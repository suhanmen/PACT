def exchange(lst1, lst2):
    # Check if lst1 contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are no even numbers in lst2, return "NO"
    if len(even_nums) == 0:
        return "NO"
    
    # Find the odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # If there are no odd numbers in lst1, return "YES"
    if len(odd_nums) == 0:
        return "YES"
    
    # Exchange an odd number in lst1 with an even number in lst2
    lst1[lst1.index(odd_nums[0])] = even_nums[0]
    lst2[lst2.index(even_nums[0])] = odd_nums[0]
    
    # Recursively call the function with the updated lists
    return exchange(lst1, lst2)
