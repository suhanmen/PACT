def even_odd_palindrome(n):
    # Initialize the count of even and odd palindromes to zero
    even_count, odd_count = 0, 0
    
    # Loop through all numbers from 1 to n
    for i in range(1, n+1):
        # Convert the number to a string and reverse it
        reverse_str = str(i)[::-1]
        
        # If the reversed string equals the original string, it is a palindrome
        if str(i) == reverse_str:
            # If the number of digits is even, increment the even count, otherwise increment the odd count
            if len(str(i)) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    # Return the tuple with the even and odd counts
    return (even_count, odd_count)
