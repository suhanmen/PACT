Here is the completed code snippet:

```python
def even_Power_Sum(n):
    sum = 0
    count = 0
    num = 2
    while count < n:
        sum += num ** 5
        num += 2
        count += 1
    return sum

assert even_Power_Sum(2) == 1056
```

In this code, we initialize the sum variable to 0 and the count variable to 0. We also initialize the num variable to 2, as we want to start with the first even natural number.

We then enter a while loop that continues until the count reaches the given input n. Inside the loop, we add the current even number raised to the fifth power to the sum variable. We also increment the num variable by 2 to get the next even number. Finally, we increment the count variable by 1.

After the loop ends, we return the sum variable, which contains the sum of the first n even natural numbers raised to the fifth power.

The assert statement at the end checks if the function returns the expected result for the given input.