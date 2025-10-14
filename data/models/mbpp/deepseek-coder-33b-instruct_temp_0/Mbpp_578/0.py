Here is the Python function to interleave 3 lists of the same length into a single flat list:

```python
def interleave_lists(list1, list2, list3):
    interleaved_list = []
    for i in range(len(list1)):
        interleaved_list.append(list1[i])
        interleaved_list.append(list2[i])
        interleaved_list.append(list3[i])
    return interleaved_list
```

You can test the function with the provided example:

```python
print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))
```

This should output:

```python
[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
```
