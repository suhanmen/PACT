def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum([1 for num in lst1 if num % 2 != 0])
    
    # Calculate the number of elements needed to be exchanged from lst2 to make lst1 all even
    exchange_count = len(lst1) - odd_count
    
    # Count the number of even elements in lst2 that can be exchanged with odd elements in lst1
    possible_exchange_count = sum([1 for num in lst2 if num % 2 == 0 and exchange_count > 0])
    
    # Determine if it is possible to exchange elements to make lst1 all even
    if possible_exchange_count >= exchange_count:
        return "YES"
    else:
        return "NO"
