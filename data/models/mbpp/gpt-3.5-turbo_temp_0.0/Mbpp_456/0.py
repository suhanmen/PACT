Here is the completed code snippet:

```python
def reverse_string_list(string_list):
    reversed_list = []
    for string in string_list:
        reversed_list.append(string[::-1])
    return reversed_list

assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
```

The `reverse_string_list` function takes a list of strings as input. It creates an empty list called `reversed_list` to store the reversed strings. Then, it iterates over each string in the input list using a for loop. For each string, it uses the slicing syntax `[::-1]` to reverse the string and appends the reversed string to the `reversed_list`. Finally, it returns the `reversed_list`.

The `assert` statement is used to check if the function produces the expected output. In this case, it checks if the output of `reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])` is equal to `['deR', 'neerG', 'eulB', 'etihW', 'kcalB']`. If the condition is true, the program continues execution. If the condition is false, an AssertionError is raised.