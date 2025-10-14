Here is the completed code snippet:

```python
def first_non_repeating_character(string):
    char_count = {}
    
    # Count the occurrences of each character in the string
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first character with count 1
    for char in string:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character is found, return None
    return None

# Test the function
assert first_non_repeating_character("abcabc") == None
```

This function takes a string as input and returns the first non-repeating character in the string. It uses a dictionary to count the occurrences of each character in the string. Then, it iterates through the string again to find the first character with a count of 1. If no non-repeating character is found, it returns None.