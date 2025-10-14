def exchange(lst1, lst2):
    # Check if lst1 is already all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Find all the odd numbers in lst1 and their corresponding even numbers in lst2
    odd_nums = [num for num in lst1 if num % 2 != 0]
    even_nums = [num for num in lst2 if num % 2 == 0 and num not in lst1]

    # If there aren't enough even numbers in lst2 to replace all the odd numbers in lst1, return "NO"
    if len(odd_nums) > len(even_nums):
        return "NO"

    # Exchange the odd numbers in lst1 with the even numbers in lst2
    for i in range(len(odd_nums)):
        lst1[lst1.index(odd_nums[i])] = even_nums[i]

    # Check if lst1 is now all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
