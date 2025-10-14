def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    # If there are no odd elements in lst1, then it's already a list of even numbers
    if odd_count == 0:
        return "YES"
    # Count the number of even elements in lst2
    even_count = sum(1 for num in lst2 if num % 2 == 0)
    # If there are not enough even elements in lst2 to replace the odd elements in lst1, return "NO"
    if even_count < odd_count:
        return "NO"
    # Sort lst1 and lst2 in ascending order
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    # Replace the odd elements in lst1 with the even elements in lst2
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    break
    # Check if lst1 is now a list of even numbers
    if sum(1 for num in lst1 if num % 2 != 0) == 0:
        return "YES"
    else:
