def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)

    # Count the number of even elements in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)

    # Check if the number of odd elements in lst1 is less than or equal to the number of even elements in lst2
    if odd_count <= even_count:
        return "YES"
    else:
        return "NO"
