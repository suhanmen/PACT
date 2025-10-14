def exchange(lst1, lst2):
    evens_in_lst1 = [num for num in lst1 if num % 2 == 0]
    odds_in_lst2 = [num for num in lst2 if num % 2 == 1]
    
    if len(evens_in_lst1) == len(lst1):
        # lst1 is already all even numbers
        return "YES"
    
    if len(odds_in_lst2) < len(lst1) - len(evens_in_lst1):
        # there aren't enough odd numbers in lst2 to exchange
        return "NO"
    
    return "YES"
