def exchange(lst1, lst2):
    # Check if lst1 already has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Find the odd numbers in lst1 and the even numbers in lst2
    odd_nums_lst1 = [num for num in lst1 if num % 2 == 1]
    even_nums_lst2 = [num for num in lst2 if num % 2 == 0]

    # Check if there are enough even numbers in lst2 to replace all the odd numbers in lst1
    if len(odd_nums_lst1) > len(even_nums_lst2):
        return "NO"

    return "YES"
