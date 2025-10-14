def get_max_triples(n):
    # initialize the array a using list comprehension
    a = [i*i-i+1 for i in range(1, n+1)]
    count = 0
    # iterate over all possible combinations of i, j, k
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                # check if the sum of a[i], a[j], a[k] is a multiple of 3
                if (a[i]+a[j]+a[k]) % 3 == 0:
                    count += 1
    return count
