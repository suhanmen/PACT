Here is the completed code snippet:

```python
def subject_marks(lst):
    return sorted(lst, key=lambda x: x[1])

assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
```

The `subject_marks` function takes a list of tuples as input. It uses the `sorted` function to sort the list based on the second value of each tuple. The `key` parameter is set to a lambda function that returns the second value of each tuple (`x[1]`). This lambda function is used as the sorting key, so the list is sorted based on the second value of each tuple.

The `assert` statement is used to verify that the function returns the expected output.