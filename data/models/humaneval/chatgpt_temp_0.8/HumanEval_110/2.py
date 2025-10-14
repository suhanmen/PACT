def exchange(lst1, lst2):
    evens = [num for num in lst1 if num % 2 == 0] # get all even numbers from lst1
    if len(evens) == len(lst1): # if lst1 already only contains even numbers, return "YES"
        return "YES"
    for num in lst2: # check each number in lst2
        if num % 2 == 0 and num not in lst1: # if the number is even and not already in lst1, add it to lst1
            lst1.append(num)
            evens = [num for num in lst1 if num % 2 == 0] # update the list of even numbers in lst1
            if len(evens) == len(lst1): # if lst1 now only contains even numbers, return "YES"
                return "YES"
    return "NO" # if all numbers in lst2 have been checked and lst1 still doesn't only contain even numbers, return "NO"
