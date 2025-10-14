Here is the completed code snippet:

```python
def validate(num):
    num_str = str(num)
    for digit in num_str:
        if int(digit) < num_str.count(digit):
            return False
    return True

assert validate(1234) == True
```