Here is the Python function to reverse only the vowels of a given string:

```python
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)
```

This function works by using two pointers, one at the start of the string and one at the end. It then iterates through the string, swapping the vowels at the two pointers. If the character at the start or end is not a vowel, it moves the pointer inwards. This continues until the two pointers meet in the middle of the string.

You can test the function with the following code:

```python
print(reverse_vowels("Python"))  # Output: "Python"
```

This will output "Python" as the function does not reverse the vowels in the string "Python" as there are no vowels to reverse.
