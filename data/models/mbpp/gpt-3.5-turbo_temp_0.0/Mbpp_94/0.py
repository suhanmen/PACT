Here is the completed code snippet:

```python
def index_minimum(lst):
    min_second_value = float('inf')
    min_tuple = None
    
    for tuple in lst:
        if tuple[1] < min_second_value:
            min_second_value = tuple[1]
            min_tuple = tuple
    
    return min_tuple[0]

assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
```

In this code, we initialize `min_second_value` to positive infinity and `min_tuple` to `None`. We then iterate through each tuple in the list. If the second value of the current tuple is smaller than `min_second_value`, we update `min_second_value` and `min_tuple` to the current tuple. Finally, we return the first value of `min_tuple`.