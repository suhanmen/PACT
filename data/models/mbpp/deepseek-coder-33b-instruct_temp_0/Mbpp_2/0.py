Here is the Python function implemented in a markdown style code block:

```python
def similar_elements(list1, list2):
    return [i for i in list1 if i in list2]

print(set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))))
```

This function uses list comprehension to iterate over the first list and check if each element is in the second list. If it is, it adds it to the new list. The function then returns this new list.

The print statement at the end is used to test the function with the provided example. It converts the result to a set to remove any duplicate elements, as sets only contain unique elements.
