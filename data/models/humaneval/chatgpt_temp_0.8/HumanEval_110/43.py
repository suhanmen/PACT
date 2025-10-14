def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(lst2) < len(odd_indices):
        return "NO"
    
    # Replace the odd numbers in lst1 with even numbers from lst2
    for i in odd_indices:
        for j, num in enumerate(lst2):
            if num % 2 == 0:
                lst1[i] = num
                lst2[j] = float('inf')  # Mark the even number as used
                break
    
    # Check if lst1 now contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
