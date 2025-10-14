def exchange(lst1, lst2):
    # Check if lst1 already has all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if there are any even numbers in lst2 that can be exchanged with odd numbers in lst1
    for num2 in lst2:
        if num2 % 2 == 0:
            for i, num1 in enumerate(lst1):
                if num1 % 2 != 0:
                    lst1[i] = num2
                    break
            else:
                continue
            if all(num % 2 == 0 for num in lst1):
                return "YES"
    
    # If no exchange is possible, return "NO"
    return "NO"
