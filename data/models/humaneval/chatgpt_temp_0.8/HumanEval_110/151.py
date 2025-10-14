def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Find all odd numbers in lst1
    odd_nums = [num for num in lst1 if num % 2 != 0]

    # Find all even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]

    # If the number of odd numbers in lst1 is greater than the number of even numbers in lst2, return "NO"
    if len(odd_nums) > len(even_nums):
        return "NO"

    # Otherwise, return "YES"
    return "YES"
