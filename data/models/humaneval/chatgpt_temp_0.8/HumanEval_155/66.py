def even_odd_count(num):
    even_count = 0
    odd_count = 0

    # converting the number to a string
    num_str = str(num)

    # iterating over each character in the string
    for char in num_str:
        # checking if the character is a digit
        if char.isdigit():
            # converting the character to an integer
            digit = int(char)
            # checking if the digit is even or odd
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
