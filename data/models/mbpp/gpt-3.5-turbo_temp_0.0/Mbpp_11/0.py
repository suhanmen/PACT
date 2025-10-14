Here is the completed code snippet:

```python
def remove_Occ(string, char):
    first_occurrence = string.find(char)
    last_occurrence = string.rfind(char)
    
    if first_occurrence != -1 and last_occurrence != -1:
        return string[:first_occurrence] + string[first_occurrence+1:last_occurrence] + string[last_occurrence+1:]
    else:
        return string

assert remove_Occ("hello", "l") == "heo"
```

In this code, the `remove_Occ` function takes two parameters: `string` and `char`. It uses the `find` method to find the index of the first occurrence of the given character in the string, and the `rfind` method to find the index of the last occurrence of the given character in the string.

If both the first and last occurrences are found, it removes the first occurrence by slicing the string from the start to the index of the first occurrence, and concatenates it with the sliced string from the index of the first occurrence + 1 to the index of the last occurrence, and finally concatenates it with the sliced string from the index of the last occurrence + 1 to the end of the string.

If either the first or last occurrence is not found, it returns the original string as it is.

The `assert` statement is used to check if the function returns the expected output. In this case, it checks if `remove_Occ("hello", "l")` returns `"heo"`.