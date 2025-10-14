def exchange(lst1, lst2):
    odds = [i for i in lst1 if i % 2 == 1] # get the odd numbers in lst1
    evens = [i for i in lst2 if i % 2 == 0] # get the even numbers in lst2
    if len(odds) > len(evens): # if there are more odds than evens, it's impossible to exchange
        return "NO"
    else:
        return "YES"
