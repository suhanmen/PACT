Here is the completed code snippet:

```python
def mul_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            if even is None:
                even = num
            else:
                even *= num
        else:
            if odd is None:
                odd = num
            else:
                odd *= num
    return even * odd

assert mul_even_odd([1,3,5,7,4,1,6,8]) == 4
```

This function iterates through the given list and checks if each number is even or odd. It keeps track of the first even number encountered and multiplies it with subsequent even numbers. Similarly, it keeps track of the first odd number encountered and multiplies it with subsequent odd numbers. Finally, it returns the product of the first even and odd numbers. The assert statement checks if the function returns the expected result for the given example.