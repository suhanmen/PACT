def exchange(lst1, lst2):
    # Count the number of odd integers in lst1
    odd_count = sum([1 for i in lst1 if i % 2 == 1])
    
    # Count the number of even integers in lst2
    even_count = sum([1 for i in lst2 if i % 2 == 0])
    
    # If the number of odd integers in lst1 is greater than the number of even integers in lst2,
    # then it is not possible to exchange elements to make lst1 a list of only even numbers
    if odd_count > even_count:
        return "NO"
    else:
        return "YES"
