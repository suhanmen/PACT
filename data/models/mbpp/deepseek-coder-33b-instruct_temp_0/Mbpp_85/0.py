Sure, here is the Python function to find the surface area of a sphere:

```python
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2
```

You can use the `math.isclose` function to check if the result is close to the expected value. Here is how you can do it:

```python
import math

def test_surfacearea_sphere():
    assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)

test_surfacearea_sphere()
```

This will raise an `AssertionError` if the result is not close to the expected value. If no error is raised, it means the function is working correctly.
