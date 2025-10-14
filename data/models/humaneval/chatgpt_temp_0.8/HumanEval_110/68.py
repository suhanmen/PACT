def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)

    # Count the number of even numbers in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)

    # If there are more odd numbers in lst1 than even numbers in lst2, return "NO"
    if odd_count > even_count:
        return "NO"

    # Otherwise, it is possible to make lst1 all even by exchanging elements with lst2
    return "YES"
