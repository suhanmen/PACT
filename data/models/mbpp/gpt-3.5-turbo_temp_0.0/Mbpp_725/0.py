Here is the completed code snippet:

```python
def extract_quotation(string):
    import re
    return re.findall(r'"([^"]*)"', string)

assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
```

The `extract_quotation` function uses the `re.findall` method from the `re` module to find all occurrences of text between quotation marks in the given string. The regular expression pattern `r'"([^"]*)"' matches any text between two quotation marks and captures it as a group. The `findall` method returns a list of all the captured groups, which are the values between quotation marks in the string.