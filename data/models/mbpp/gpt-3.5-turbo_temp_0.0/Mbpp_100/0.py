Here's the completed code snippet:

```python
def next_smallest_palindrome(num):
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num

assert next_smallest_palindrome(99) == 101
```

In this code, we start by incrementing the given number by 1. Then, we enter a while loop that checks if the string representation of the number is equal to its reverse. If not, we increment the number by 1 and continue the loop. Once we find a palindrome, we return it. The assert statement at the end verifies that the function returns the expected result for the given example.