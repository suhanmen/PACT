def generate_integers(a, b):
    # convert a and b to strings
    a_str = str(a)
    b_str = str(b)

    # determine the range of numbers to check
    if a < b:
        start = int(a_str[0]) + 1 if int(a_str[0]) % 2 == 0 else int(a_str[0]) + 2
        end = int(b_str[0]) - 1 if int(b_str[0]) % 2 == 0 else int(b_str[0]) - 2
    else:
        start = int(b_str[0]) + 1 if int(b_str[0]) % 2 == 0 else int(b_str[0]) + 2
        end = int(a_str[0]) - 1 if int(a_str[0]) % 2 == 0 else int(a_str[0]) - 2

    # generate the list of even digits
    evens = []
    for i in range(start, end+1, 2):
        evens.append(i)
    
    return evens
