def exchange(lst1, lst2):
    # Determine whether lst1 contains only even numbers
    all_even = all(num % 2 == 0 for num in lst1)
    if all_even:
        return "YES"
    
    # Determine which elements can be exchanged to make lst1 all even
    exchangeable = [num for num in lst2 if num % 2 == 0 and num not in lst1]
    exchangeable_count = len(exchangeable)
    if exchangeable_count == 0:
        return "NO"
    
    # Determine whether the number of exchangeable elements is enough
    needed_exchanges = sum(1 for num in lst1 if num % 2 != 0)
    if exchangeable_count >= needed_exchanges:
        return "YES"
    else:
        return "NO"
