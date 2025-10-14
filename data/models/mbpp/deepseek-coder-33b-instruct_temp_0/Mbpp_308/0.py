Here is the Python function that solves the problem:

```python
def large_product(list1, list2, n):
    # Sort the lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)

    # Initialize an empty list to store the products
    products = []

    # Calculate the products of the largest numbers from each list
    for i in range(n):
        product = list1[i] * list2[i]
        products.append(product)

    # Return the list of products
    return products

# Test the function
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))
```

This function works by first sorting the input lists in descending order. Then, it calculates the product of the largest numbers from each list and adds it to the list of products. Finally, it returns the list of products.

Please note that this function assumes that the input lists have at least 'n' elements. If this is not the case, you may want to add error checking code to handle this situation.
