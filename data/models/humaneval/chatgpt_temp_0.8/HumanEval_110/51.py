def exchange(lst1, lst2):
    # Check if lst1 already contains all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
  
    # Find all odd numbers in lst1 and their corresponding indices
    odd_nums = [num for num in lst1 if num % 2 != 0]
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]
  
    # Find all even numbers in lst2
    even_nums = [num for num in lst2 if num % 2 == 0]
  
    # Check if there are enough even numbers in lst2 to replace all odd numbers in lst1
    if len(even_nums) < len(odd_nums):
        return "NO"
  
    # Replace odd numbers in lst1 with even numbers from lst2
    for i, num in zip(odd_indices, even_nums):
        lst1[i] = num
  
    # Check if all numbers in lst1 are even now
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
