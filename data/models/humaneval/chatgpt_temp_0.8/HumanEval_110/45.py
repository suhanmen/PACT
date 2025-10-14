def exchange(lst1, lst2):
    # Check if lst1 already consists of only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # Find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace all the odd numbers in lst1,
    # then it is impossible to make lst1 a list of only even numbers
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Sort both lists in descending order of the difference between the value and the nearest even number
    odd_nums.sort(key=lambda num: abs(num - round(num/2)*2), reverse=True)
    even_nums.sort(key=lambda num: abs(num - round(num/2)*2), reverse=True)
    
    # Swap the odd numbers in lst1 with the even numbers in lst2 based on the sorting order
    for i in range(len(odd_nums)):
        if abs(odd_nums[i] - round(odd_nums[i]/2)*2) > abs(even_nums[i] 
