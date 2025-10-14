Here is the completed code snippet:

```python
def extract_values(string):
    values = []
    start = 0
    while True:
        start = string.find('"', start) + 1
        end = string.find('"', start)
        if start == 0 or end == -1:
            break
        values.append(string[start:end])
        start = end + 1
    return values

assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
```

This function uses a while loop to iterate through the string and find the indices of the quotation marks. It then extracts the values between the quotation marks and appends them to the `values` list. The loop continues until there are no more quotation marks found. Finally, the function returns the `values` list.