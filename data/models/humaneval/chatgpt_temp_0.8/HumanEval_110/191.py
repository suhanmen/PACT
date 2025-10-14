python
def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Find the indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 == 1]

    # Find the indices of even numbers in lst2
    even_indices = [i for i, num in enumerate(lst2) if num % 2 == 0]

    # Check if there are enough even numbers in lst2 to replace odd numbers in lst1
    if len(even_indices) >= len(odd_indices):
        return "YES"
    else:
        return "NO"
