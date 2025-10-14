def exchange(lst1, lst2):
    # Check if lst1 is already all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1
    odds = [num for num in lst1 if num % 2 != 0]
    
    # Find the even numbers in lst2
    evens = [num for num in lst2 if num % 2 == 0]
    
    # Check if there are enough evens in lst2 to replace the odds in lst1
    if len(odds) > len(evens):
        return "NO"
    
    # If there are enough evens, replace the odd numbers in lst1 with evens from lst2
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            if evens:
                lst1[i] = evens.pop(0)
            else:
                break
    
    # Check if lst1 is now all even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"
