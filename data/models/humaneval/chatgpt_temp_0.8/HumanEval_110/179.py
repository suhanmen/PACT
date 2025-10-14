def exchange(lst1, lst2):
    # Check if all elements of lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Find the indices of odd numbers in lst1
    odd_indices = [i for i, num in enumerate(lst1) if num % 2 != 0]

    # Find the indices of even numbers in lst2
    even_indices = [i for i, num in enumerate(lst2) if num % 2 == 0]

    # Check if there are enough even numbers in lst2 to replace the odd numbers in lst1
    if len(even_indices) < len(odd_indices):
        return "NO"

    # Exchange the odd numbers in lst1 with even numbers in lst2
    for i in range(len(odd_indices)):
        j = i  # Start searching for even number from the same index
        while j < len(even_indices) and lst2[even_indices[j]] <= lst1[odd_indices[i]]:
            j += 1
        if j == len(even_indices):
            return "NO"  # No even number found to exchange with odd number
        else:
            lst1[odd_indices[i]], lst2[even_indices[j]] = lst2[even_indices[j]], lst1[odd_ind
