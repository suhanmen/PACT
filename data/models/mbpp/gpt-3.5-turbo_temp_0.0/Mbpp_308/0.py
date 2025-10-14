Here is the completed code snippet:

```python
def large_product(list1, list2, num):
    products = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            products.append(list1[i] * list2[j])
    products.sort(reverse=True)
    return products[:num]

assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]
```

In this code, the `large_product` function takes two lists (`list1` and `list2`) and a number (`num`) as input. It calculates the product of each pair of elements from the two lists and stores them in the `products` list. Then, it sorts the `products` list in descending order and returns the first `num` elements.

The `assert` statement at the end of the code verifies that the function returns the expected result for the given example.