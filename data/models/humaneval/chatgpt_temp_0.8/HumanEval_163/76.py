def generate_integers(a, b):
    # initialize empty list to store even digits
    even_digits = []
    # loop through range of numbers between a and b (inclusive)
    for num in range(a, b + 1):
        # convert number to string to access each digit
        num_str = str(num)
        # loop through each digit in the string
        for digit in num_str:
            # check if digit is even and not already in the even_digits list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                # add even digit to list
                even_digits.append(int(digit))
    # sort the list in ascending order
    even_digits.sort()
    # return the list of even digits
    return even_digits
