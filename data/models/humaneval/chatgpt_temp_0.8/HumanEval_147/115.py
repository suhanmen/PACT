def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]
    count = 0
    mod_counts = [0] * 3
    for num in a:
        mod_counts[num % 3] += 1
    count += (mod_counts[0] * (mod_counts[0] - 1) * (mod_counts[0] - 2)) // 6
    count += (mod_counts[1] * mod_counts[2] * mod_counts[0])
    count += (mod_counts[1] * (mod_counts[1] - 1) * (mod_counts[1] - 2)) // 6
    count += (mod_counts[2] * (mod_counts[2] - 1) * (mod_counts[2] - 2)) // 6
    count += (mod_counts[1] * (mod_counts[1] - 1) * mod_counts[0]) // 2
    count += (mod_counts[2] * (mod_counts[2] - 1) * mod_counts[0]) // 2
    return count
