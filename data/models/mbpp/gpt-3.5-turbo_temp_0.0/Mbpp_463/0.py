Here is the completed code snippet:

```python
def max_subarray_product(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = max_product
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
```

In this code, we initialize `max_product` and `min_product` to the first element of the array. We also initialize `result` to `max_product` as the initial maximum product subarray.

We then iterate through the array starting from the second element. If the current element is negative, we swap `max_product` and `min_product` because multiplying a negative number with the current `max_product` will give us a smaller product, while multiplying it with the current `min_product` will give us a larger product.

We update `max_product` and `min_product` by taking the maximum and minimum of the current element and the product of the current element and the previous `max_product` and `min_product` respectively.

Finally, we update `result` to the maximum of `result` and `max_product` at each iteration.

At the end of the loop, `result` will contain the maximum product subarray.