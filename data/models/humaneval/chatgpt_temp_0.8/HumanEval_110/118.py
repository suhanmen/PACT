python
def exchange(lst1, lst2):
    # Find the count of odd numbers in lst1
    odd_count = sum(1 for num in lst1 if num % 2 == 1)
    # Find the count of even numbers in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    # If the count of odd numbers in lst1 is greater than the count of even numbers in lst2, return "NO"
    if odd_count > even_count:
        return "NO"
    # Otherwise, return "YES"
    return "YES"
