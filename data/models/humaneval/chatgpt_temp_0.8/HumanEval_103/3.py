def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) / 2  # Compute the average
    rounded_avg = round(avg)  # Round to the nearest integer
    binary_avg = bin(rounded_avg)  # Convert to binary
    return binary_avg
