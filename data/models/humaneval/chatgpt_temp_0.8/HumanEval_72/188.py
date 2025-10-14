def will_it_fly(q,w):
    # find the sum of the elements in q
    sum_of_elements = sum(q)
    
    # check if q is a palindrome
    if q == q[::-1]:
        # check if the sum of elements is less than or equal to w
        if sum_of_elements <= w:
            return True
        else:
            return False
    else:
        return False
