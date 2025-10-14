def solve(s):
    # Check if the string contains no letters
    if s.isalpha() == False:
        return s[::-1]
    else:
        # Reverse the case of each letter in the string
        new_s = ""
        for letter in s:
            if letter.islower():
                new_s += letter.upper()
            elif letter.isupper():
                new_s += letter.lower()
            else:
                new_s += letter
        return new_s
