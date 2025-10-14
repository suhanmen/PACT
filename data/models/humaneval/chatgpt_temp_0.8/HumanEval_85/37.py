def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..
    
    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total = 0
    for i in range(1,len(lst),2):   # iterating over odd indices
        if lst[i] % 2 == 0:         # checking if the element at the odd index is even
            total += lst[i]         # adding the even element to the total
    return total
