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
    a = [i*i - i + 1 for i in range(1, n+1)]

    # Initialize variables
    count = 0
    mod_0 = 0
    mod_1 = 0
    mod_2 = 0

    # Count the number of elements that give a remainder of 0, 1, or 2 when divided by 3
    for i in range(n):
        if a[i] % 3 == 0:
            mod_0 += 1
        elif a[i] % 3 == 1:
            mod_1 += 1
        else:
            mod_2 += 1

    # Count the number of valid triples
    count += mod_0 * (mod_0 - 1) * (mod_0 - 2) // 6
    count += mod_1 * mod_2 * (mod_2 - 1) // 2
    count += mod_1 * (mod_1 - 1) * (mod_1 - 2) // 6
    count += mod_2 * (mod_2 - 1) * (mod_2 - 2) // 6
    count += mod_0 * mod_1 * mod_2

    # Return the number of valid triples
    return count
