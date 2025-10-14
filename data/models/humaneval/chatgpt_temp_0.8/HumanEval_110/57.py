def exchange(lst1, lst2):
    # First, check if lst1 already contains all even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # If lst1 contains odd numbers, try to exchange elements from lst2
    for num2 in lst2:
        if num2 % 2 == 0:
            # Find the first odd number in lst1 and exchange it with num2
            for i, num1 in enumerate(lst1):
                if num1 % 2 == 1:
                    lst1[i] = num2
                    break
            else:
                # If no odd number is found in lst1, return "NO"
                return "NO"

            # If the exchange is made, check if lst1 now contains all even numbers
            if all(num % 2 == 0 for num in lst1):
                return "YES"

    # If all elements in lst2 have been checked and lst1 still contains odd numbers,
    # return "NO"
    return "NO"
