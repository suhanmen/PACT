python
def iscube(a):
    # Take the absolute value of a to handle negative inputs
    a = abs(a)
    # Find the cube root of a using the ** operator
    root = a**(1/3)
    # Check if the cube root is an integer
    return root == int(root)
