Here is the completed code snippet:

```python
def rectangle_area(length, width):
    """
    Calculates the area of a rectangle given its length and width.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

assert rectangle_area(10, 20) == 200
```

The `rectangle_area` function takes in two parameters, `length` and `width`, and returns the product of the two values, which represents the area of the rectangle. The `assert` statement is used to verify that the function returns the expected result of 200 when called with arguments 10 and 20.