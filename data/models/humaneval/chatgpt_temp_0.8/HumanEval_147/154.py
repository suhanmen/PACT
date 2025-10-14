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

    # Create the array a
    a = [i * i - i + 1 for i in range(1, n+1)]

    # Initialize variables
    count = 0
    freq = [0] * 3

    # Count the number of elements that give remainder 0, 1, or 2 when divided by 3
    for i in range(n):
        freq[a[i] % 3] += 1

    # Count the number of valid triples
    for i in range(n):
        freq[a[i] % 3] -= 1
        count += freq[(3 - a[i] % 3) % 3]

    return count
