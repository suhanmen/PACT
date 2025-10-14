def exchange(lst1, lst2):
    # check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # find the even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
    
    # check if there are enough even numbers in lst2 to make lst1 all even
    if len(even_nums) < len(lst1) - sum(num % 2 == 0 for num in lst1):
        return "NO"
    
    # if there are enough even numbers, return "YES"
    return "YES"
