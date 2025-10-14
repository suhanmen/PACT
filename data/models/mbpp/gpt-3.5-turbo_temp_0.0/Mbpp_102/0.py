Here is the completed code snippet:

```python
def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0].capitalize()
    for word in words[1:]:
        camel_case_string += word.capitalize()
    return camel_case_string

assert snake_to_camel('python_program') == 'PythonProgram'
```

In this code, we first split the snake case string into individual words using the `split('_')` method. Then, we capitalize the first word and append it to the `camel_case_string` variable. Finally, we iterate over the remaining words, capitalize each one, and append it to the `camel_case_string`. The resulting `camel_case_string` is then returned.