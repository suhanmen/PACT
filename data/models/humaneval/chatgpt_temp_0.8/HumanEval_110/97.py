def exchange(lst1, lst2):
    # count the number of odd numbers in lst1
    odd_count = sum([1 for num in lst1 if num % 2 != 0])
    
    # count the number of even numbers in lst2
    even_count = sum([1 for num in lst2 if num % 2 == 0])
    
    # check if it is possible to exchange elements between lst1 and lst2
    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"
