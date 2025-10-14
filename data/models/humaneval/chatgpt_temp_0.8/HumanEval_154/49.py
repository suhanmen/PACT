def cycpattern_check(a , b):
    # Find the length of the two input strings
    len_a = len(a)
    len_b = len(b)
    
    # Check if the length of b is greater than a
    if len_b > len_a:
        return False
    
    # Concatenate a with itself to form a new string
    new_a = a + a
    
    # Check if b or any of its rotations is a substring in new_a
    for i in range(len_a):
        if new_a[i:i+len_b] == b:
            return True
    
    return False
