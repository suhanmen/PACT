Here is the Python function to convert a snake case string to camel case string:

```python
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)
```

You can test the function with the following code:

```python
print(snake_to_camel('python_program'))  # Output: PythonProgram
```
