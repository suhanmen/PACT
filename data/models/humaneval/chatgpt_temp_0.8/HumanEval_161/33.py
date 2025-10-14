def solve(s):
    # Check if the string contains any letters
    if not any(c.isalpha() for c in s):
        # If it doesn't, reverse the string
        return s[::-1]
    
    # Create an empty list to store the modified characters
    new_s = []
    
    # Loop through each character in the string
    for c in s:
        # If the character is a letter, reverse its case
        if c.isalpha():
            if c.islower():
                new_s.append(c.upper())
            else:
                new_s.append(c.lower())
        else:
            # If it's not a letter, keep it as it is
            new_s.append(c)
            
    # Convert the list of characters back into a string and return it
    return "".join(new_s)
