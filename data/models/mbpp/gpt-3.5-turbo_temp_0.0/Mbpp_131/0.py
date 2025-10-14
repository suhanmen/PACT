Here is the completed code snippet:

```python
def reverse_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = list(string)
    i, j = 0, len(string) - 1

    while i < j:
        if string[i] in vowels and string[j] in vowels:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        elif string[i] in vowels:
            j -= 1
        elif string[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1

    return ''.join(string)

assert reverse_vowels("Python") == "Python"
```

This function takes a string as input and reverses only the vowels in the string. It uses two pointers, `i` and `j`, starting from the beginning and end of the string respectively. It checks if the characters at these positions are vowels. If both are vowels, it swaps them and moves the pointers towards the center. If only one of them is a vowel, it moves the corresponding pointer towards the center. If neither of them is a vowel, it moves both pointers towards the center. Finally, it returns the modified string.