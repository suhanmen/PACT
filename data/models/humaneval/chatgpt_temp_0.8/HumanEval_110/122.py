def exchange(lst1, lst2):
    # check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # find all even numbers in lst2 that could be exchanged with odd numbers in lst1
    even_nums = [num for num in lst2 if num % 2 == 0 and num not in lst1]

    # count the number of odd numbers in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)

    # check if there are enough even numbers in lst2 to exchange with all the odd numbers in lst1
    if odd_count <= len(even_nums):
        return "YES"
    else:
        return "NO"
