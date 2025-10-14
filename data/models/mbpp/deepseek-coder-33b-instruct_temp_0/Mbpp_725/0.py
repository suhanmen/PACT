Here is the Python function to extract values between quotation marks " " of the given string:

```python
import re

def extract_quotation(s):
    return re.findall(r'"([^"]*)"', s)
```

This function uses the `re` module in Python, which provides support for regular expressions. The `findall` function is used to find all substrings where the regular expression matches, and returns them as a list. The regular expression `r'"([^"]*)"'` matches any string that starts with a quote, followed by any number of characters that are not a quote, and ends with a quote. The parentheses around `[^"]*` create a group that `findall` returns.

You can test this function with the provided test case:

```python
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
```

This should output:

```python
['A53', 'multi', 'Processor']
```
