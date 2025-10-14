Here is the completed code snippet:

```python
def find_sum(lst):
    non_repeated_elements = []
    for num in lst:
        if lst.count(num) == 1:
            non_repeated_elements.append(num)
    return sum(non_repeated_elements)

assert find_sum([1,2,3,1,1,4,5,6]) == 21
```

In this code, we define a function `find_sum` that takes a list `lst` as input. We initialize an empty list `non_repeated_elements` to store the non-repeated elements. 

We then iterate over each element `num` in the input list `lst`. Using the `count` method, we check if the count of `num` in `lst` is equal to 1. If it is, it means that `num` is a non-repeated element, so we append it to the `non_repeated_elements` list.

Finally, we return the sum of the `non_repeated_elements` list using the `sum` function.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example.