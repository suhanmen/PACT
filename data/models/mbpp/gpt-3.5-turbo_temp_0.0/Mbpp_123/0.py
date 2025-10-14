Here is the completed code snippet:

```python
def amicable_numbers_sum(n):
    def sum_of_divisors(num):
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum

    amicable_sum = 0
    for i in range(1, n+1):
        sum1 = sum_of_divisors(i)
        sum2 = sum_of_divisors(sum1)
        if i == sum2 and i != sum1:
            amicable_sum += i

    return amicable_sum

assert amicable_numbers_sum(999) == 504
```

The `amicable_numbers_sum` function takes a number `n` as input and returns the sum of all amicable numbers from 1 to `n`. 

The `sum_of_divisors` function is a helper function that calculates the sum of proper divisors of a given number.

The main logic of the `amicable_numbers_sum` function is to iterate through all numbers from 1 to `n`. For each number, it calculates the sum of its proper divisors (`sum1`). Then, it calculates the sum of proper divisors of `sum1` (`sum2`). If `i` is equal to `sum2` and `i` is not equal to `sum1`, then `i` and `sum1` are amicable numbers. The function adds `i` to the `amicable_sum` variable.

Finally, the function returns the `amicable_sum` as the result. The `assert` statement is used to verify that the function returns the expected result for the given test case.