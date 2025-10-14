Here is the completed code snippet:

```python
def removezero_ip(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split('.')
    
    # Remove leading zeroes from each octet
    octets = [str(int(octet)) for octet in octets]
    
    # Join the octets back together with periods
    new_ip_address = '.'.join(octets)
    
    return new_ip_address

assert removezero_ip("216.08.094.196") == '216.8.94.196'
```

This function splits the IP address into its octets using the `split()` method, removes leading zeroes from each octet using the `int()` and `str()` functions, and then joins the octets back together with periods using the `join()` method. The resulting IP address is returned. The `assert` statement checks that the function produces the expected output for the given example.