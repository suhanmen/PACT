def exchange(lst1, lst2):
    # check if lst1 already has only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # find all even numbers in lst2 and their corresponding odd numbers in lst1
    even_nums = [num for num in lst2 if num % 2 == 0]
    odd_nums = [num for num in lst1 if num % 2 != 0]
    
    # if there are not enough even numbers in lst2, return "NO"
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # sort the even and odd number lists in ascending order
    even_nums.sort()
    odd_nums.sort()
    
    # swap the odd numbers with even numbers from lst2 until lst1 has only even numbers
    for i in range(len(odd_nums)):
        if even_nums[i] > odd_nums[i]:
            lst1[lst1.index(odd_nums[i])] = even_nums[i]
        else:
            break
    
    # check if lst1 now has only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
