Here is the completed code snippet:

```python
def max_Product(arr):
    if len(arr) < 2:
        return "Array should have at least 2 elements"
    
    max_product = float('-inf')
    max_pair = ()
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_pair = (arr[i], arr[j])
    
    return max_pair

assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
```

This function iterates through the given array and calculates the product of each pair of elements. It keeps track of the maximum product found so far and the corresponding pair. Finally, it returns the pair with the highest product.