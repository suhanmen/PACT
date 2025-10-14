def solve(s):
    reversed_string = s[::-1] #reverse the string
    new_string = ""
    for char in reversed_string:
        if char.isalpha(): #check if the character is a letter
            if char.islower(): #reverse the case from lower to upper
                new_string += char.upper()
            else: #reverse the case from upper to lower
                new_string += char.lower()
        else: #keep the character as it is
            new_string += char
    return new_string
