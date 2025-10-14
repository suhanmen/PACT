Here is the completed code snippet:

```python
def count_Pairs(lst, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] != lst[j]:
                count += 1
    return count

assert count_Pairs([1,2,1],3) == 2
```

In this code, we define a function `count_Pairs` that takes a list `lst` and the length of the list `n` as parameters. We initialize a variable `count` to keep track of the number of pairs.

We use two nested loops to iterate over all possible pairs of elements in the list. The outer loop iterates from 0 to n-1, and the inner loop iterates from i+1 to n-1. This ensures that we only consider pairs where the second element is after the first element in the list.

Inside the inner loop, we check if the elements at indices i and j are unequal. If they are unequal, we increment the count by 1.

Finally, we return the count as the result.

The `assert` statement at the end of the code snippet checks if the function produces the expected result for the given example.