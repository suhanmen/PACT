def get_odd_collatz(n):
    # Initialize an empty list to store the odd numbers in collatz sequence
    odd_collatz = []

    # Define a helper function to generate the collatz sequence for a given number
    def collatz(num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3*num + 1
            sequence.append(num)
        return sequence
    
    # Generate the collatz sequence for n and add any odd numbers to the odd_collatz list
    for num in collatz(n):
        if num % 2 != 0:
            odd_collatz.append(num)
    
    # Sort the odd_collatz list in increasing order and return it
    return sorted(odd_collatz)
