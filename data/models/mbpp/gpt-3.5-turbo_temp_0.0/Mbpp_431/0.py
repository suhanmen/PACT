Here is the completed code snippet:

```
def common_element(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
```