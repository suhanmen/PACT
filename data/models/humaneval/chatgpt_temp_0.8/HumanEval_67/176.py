def fruit_distribution(s,n):
    # Find the positions of "apples" and "oranges" in the input string
    apple_pos = s.find("apples")
    orange_pos = s.find("oranges")
    
    # Extract the number of apples and oranges from the string
    num_apples = int(s[:apple_pos])
    num_oranges = int(s[orange_pos:])
    
    # Calculate the number of mangoes in the basket
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes
