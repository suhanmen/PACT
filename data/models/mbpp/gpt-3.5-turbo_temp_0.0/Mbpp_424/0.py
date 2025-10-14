Here is the completed code snippet:

```python
def extract_rear(strings):
    rear_elements = []
    for string in strings:
        rear_elements.append(string[-1])
    return rear_elements

assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
```