def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        # convert integer to string and reverse it
        str_i = str(i)
        rev_str_i = str_i[::-1]
        
        # check if the string is equal to its reverse
        if str_i == rev_str_i:
            # if the number of digits is even, increment even_count, otherwise increment odd_count
            if len(str_i) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)
