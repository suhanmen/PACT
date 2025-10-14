def exchange(lst1, lst2):
    # Check if lst1 only contains even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if there are any even numbers in lst2 that can be swapped with odd numbers in lst1
    for num1 in lst1:
        if num1 % 2 != 0:
            for num2 in lst2:
                if num2 % 2 == 0:
                    lst1[lst1.index(num1)] = num2
                    lst2[lst2.index(num2)] = num1
                    if all(num % 2 == 0 for num in lst1):
                        return "YES"
                    else:
                        # Swap back the numbers if the exchange did not result in all even numbers in lst1
                        lst1[lst1.index(num2)] = num1
                        lst2[lst2.index(num1)] = num2
                        
    # If there are no possible swaps that will result in all even numbers in lst1, return "NO"
    return "NO"
