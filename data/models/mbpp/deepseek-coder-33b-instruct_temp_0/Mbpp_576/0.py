Here is the Python function to check whether a list is a sublist of another or not:

```python
def is_Sub_Array(list1, list2):
    sub_set = False
    if list2 == []:
        sub_set = True
    elif list2 == list1:
        sub_set = True
    elif len(list2) > len(list1):
        sub_set = False
    else:
        for i in range(len(list1)):
            if list1[i] == list2[0]:
                sub_set = True
                for j in range(len(list2)):
                    if list1[i+j] != list2[j]:
                        sub_set = False
                        break
                if sub_set:
                    break
    return sub_set
```

You can test the function with the following code:

```python
print(is_Sub_Array([1,4,3,5],[1,2])) # False
print(is_Sub_Array([1,4,3,5],[1,4,3])) # True
print(is_Sub_Array([1,4,3,5],[])) # True
print(is_Sub_Array([1,4,3,5],[1,4,3,5])) # True
```

This function works by iterating over the first list and checking if the current element is the same as the first element of the second list. If it is, it then checks if the next elements in the first list are the same as the next elements in the second list. If it finds a match, it returns True. If it doesn't find a match after checking all elements, it returns False.
