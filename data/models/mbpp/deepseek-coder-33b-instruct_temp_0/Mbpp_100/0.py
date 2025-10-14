Here is the Python function to find the next smallest palindrome of a specified integer:

```python
def next_smallest_palindrome(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n
```

This function works by incrementing the input number `n` until it finds a number that is a palindrome (i.e., it reads the same forwards as backwards). It does this by converting the number to a string, reversing the string, and checking if the two are equal. If they are, it returns the number.

You can test this function with the following code:

```python
print(next_smallest_palindrome(99))  # Output: 101
```

This will print `101`, which is the next smallest palindrome after `99`.
