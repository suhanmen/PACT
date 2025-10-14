def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.

    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".

    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Convert N to a string to easily access each digit
    N_str = str(N)
    
    # Initialize a variable to hold the sum of digits
    sum_of_digits = 0
    
    # Loop through each digit in N and add it to the sum_of_digits variable
    for digit in N_str:
        sum_of_digits += int(digit)
    
    # Convert the sum_of_digits to binary format and return it as a string
    return bin(sum_of_digits)[2:]
