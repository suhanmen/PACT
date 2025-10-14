def exchange(lst1, lst2):
    # Calculate the number of odd numbers in lst1
    num_odds = sum(1 for num in lst1 if num % 2 != 0)
    
    # Calculate the number of even numbers in lst2
    num_evens = sum(1 for num in lst2 if num % 2 == 0)
    
    # If the number of odd numbers in lst1 is greater than the number of even numbers in lst2,
    # it's not possible to make lst1 a list of only even numbers
    if num_odds > num_evens:
        return "NO"
    
    # Otherwise, it's possible to make lst1 a list of only even numbers
    return "YES"
