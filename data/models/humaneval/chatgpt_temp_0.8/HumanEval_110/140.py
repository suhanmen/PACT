def exchange(lst1, lst2):
    # check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # find all the odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 == 1]
    
    # find all the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # if there are not enough even numbers in lst2 to replace the odd numbers in lst1
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # perform the exchange of elements between lst1 and lst2
    lst1 = [even_nums.pop() if num % 2 == 1 else num for num in lst1]
    
    # check if lst1 now contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
