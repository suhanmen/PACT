Here is the Python function to remove leading zeroes from an IP address:

```python
def removezero_ip(ip):
    return '.'.join(str(int(i)) for i in ip.split('.'))

# Test the function
assert removezero_ip("216.08.094.196")==('216.8.94.196')
```

This function works by splitting the IP address string into its four components using the `split('.')` method, which returns a list of the four components. It then uses a generator expression to convert each component to an integer (which removes any leading zeroes), and the `join('.')` method to reassemble the components into a string with dots between them.
