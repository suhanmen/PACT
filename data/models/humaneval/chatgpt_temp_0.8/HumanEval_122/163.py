def add_elements(arr, k):
    # Initialize the sum variable to 0
    sum = 0
    
    # Iterate through the first k elements of arr
    for i in range(k):
        # Check if the element has at most two digits
        if abs(arr[i]) < 100:
            # Add the element to the sum
            sum += arr[i]
    
    # Return the sum
    return sum
