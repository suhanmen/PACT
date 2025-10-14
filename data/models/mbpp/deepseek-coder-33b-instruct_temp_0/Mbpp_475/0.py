Here is the Python function to sort a dictionary by value:

```python
def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
```

You can test the function with the provided example:

```python
print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))
```

This should output:

```python
[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
```
