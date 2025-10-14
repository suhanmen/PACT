Here is the completed code snippet:

```python
def count_reverse_pairs(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if string_list[i] == string_list[j][::-1]:
                count += 1
    return count

assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2
```

This code defines a function `count_reverse_pairs` that takes a list of strings as input. It initializes a count variable to 0. Then, it uses nested loops to compare each pair of strings in the list. If a pair of strings is found where one is the reverse of the other, the count is incremented. Finally, the function returns the count.

The `assert` statement at the end of the code snippet checks if the function produces the expected output for the given example.