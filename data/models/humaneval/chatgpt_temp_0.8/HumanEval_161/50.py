def solve(s):
    # Check if the string contains any letters
    if not any(char.isalpha() for char in s):
        # If not, reverse the string
        return s[::-1]
    
    # If the string contains letters, manipulate them
    result = ""
    for char in s:
        if char.isalpha():
            # Reverse the case of the letter
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            # Keep non-letter characters as they are
            result += char
            
    return result
