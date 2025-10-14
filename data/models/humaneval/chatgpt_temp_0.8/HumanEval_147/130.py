def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    
    # Initialize variables to keep count of valid triples and remainder counts
    count = 0
    remainder_count = [0, 0, 0]  # counts for remainders 0, 1, 2
    
    # Generate array a and update remainder counts
    a = [i*i - i + 1 for i in range(1, n+1)]
    for num in a:
        remainder_count[num % 3] += 1
    
    # Loop through pairs of indices and check if there is a valid triple
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    
    # Adjust count based on remainder counts
    count += remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6
    count += remainder_count[1] * (remainder_count[1] - 1) * (remainder_count[1] - 2) // 6
    count += remainder_count[2] * (remainder_count[2] - 1) * (remainder_count[2] - 2) // 6
    count += remainder_count[0] * remainder_count[1] * remainder_count[2]
    
    return count
