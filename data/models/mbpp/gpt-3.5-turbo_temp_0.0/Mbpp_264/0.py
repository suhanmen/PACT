Here is the completed code snippet:

```python
def dog_age(human_age):
    if human_age <= 2:
        dog_age = human_age * 10.5
    else:
        dog_age = 21 + (human_age - 2) * 4
    return dog_age

assert dog_age(12) == 61
```

In this code, the `dog_age` function takes a human age as input and calculates the equivalent age in dog years. If the human age is less than or equal to 2, the dog age is calculated by multiplying the human age by 10.5. Otherwise, the dog age is calculated by adding 21 to the product of (human age - 2) and 4. The function then returns the calculated dog age.

The `assert` statement at the end of the code snippet checks if the `dog_age` function returns the expected result for the given input of 12. If the calculated dog age is equal to 61, the assertion passes and no error is raised.