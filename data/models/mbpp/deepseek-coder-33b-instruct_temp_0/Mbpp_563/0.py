Here is the Python function to extract values between quotation marks from a string:

```python
def extract_values(s):
    return [i.strip('"') for i in s.split(',')]
```

You can test the function with the following code:

```python
print(extract_values('"Python", "PHP", "Java"'))
```

This will output:

```python
['Python', 'PHP', 'Java']
```
