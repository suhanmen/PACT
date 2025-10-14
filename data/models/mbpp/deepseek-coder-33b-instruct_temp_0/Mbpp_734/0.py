Here is the Python function to find the sum of products of all possible sublists of a given list.

```python
def sum_Of_Subarray_Prod(lst):
    n = len(lst)
    product = 1
    res = 0
    for i in range(0, n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            res += product
    return res
```

You can test the function with the following code:

```python
print(sum_Of_Subarray_Prod([1,2,3]))  # Output: 20
```

This function works by iterating over the list and for each element, it calculates the product of all the sublists that can be formed by including that element. It then adds this product to the result. The result is the sum of products of all possible sublists.
