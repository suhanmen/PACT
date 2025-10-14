def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0] # create a list of even numbers from lst1
    sum_lst2 = sum(lst2) # get the sum of all elements in lst2
    for num in lst2:
        if (sum_lst2 + sum(even_lst1) - num) % 2 == 0: # if the sum of lst2 (excluding num) and even_lst1 is even
            return "YES" # return "YES"
    return "NO" # if no exchange can be made to make lst1 all even, return "NO"
