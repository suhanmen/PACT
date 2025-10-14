def sort_third(l: list):
    divisible_by_three = []
    for i in range(len(l)):
        if i % 3 == 0:
            divisible_by_three.append(l[i])
    divisible_by_three.sort()
    l_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime.append(divisible_by_three.pop(0))
        else:
            l_prime.append(l[i])
    return l_prime
