Here is the Python function to sort a list of tuples using the second value of each tuple:

```python
def subject_marks(lst):
    return sorted(lst, key=lambda x: x[1])
```

You can test the function with the provided example:

```python
print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))
```

This should output:

```python
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
```
