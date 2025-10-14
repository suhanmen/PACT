def exchange(lst1, lst2):
    # Check if lst1 is already all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find all odd numbers in lst1 and their indices
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    odd_numbers = [lst1[i] for i in odd_indices]
    
    # Find all even numbers in lst2
    even_numbers = [num for num in lst2 if num % 2 == 0]
    
    # If there aren't enough even numbers in lst2 to replace all odd numbers in lst1
    if len(even_numbers) < len(odd_numbers):
        return "NO"
    
    # Replace odd numbers in lst1 with even numbers from lst2
    for i in range(len(odd_indices)):
        lst1[odd_indices[i]] = even_numbers[i]
    
    # Check if lst1 is now all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
