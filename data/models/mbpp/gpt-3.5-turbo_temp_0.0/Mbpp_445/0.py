Here is the completed code snippet:

```python
def index_multiplication(tuple1, tuple2):
    result = ()
    for i in range(len(tuple1)):
        result += ((tuple1[i][0] * tuple2[i][0]), (tuple1[i][1] * tuple2[i][1]))
    return result

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
```

The `index_multiplication` function takes two tuples as input and performs index-wise multiplication of their elements. It iterates over the tuples using a for loop and multiplies the elements at each index. The result is stored in a new tuple called `result`. Finally, the function returns the `result` tuple.

The assert statement is used to verify that the function produces the expected output.