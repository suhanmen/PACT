def exchange(lst1, lst2):
    even_nums = [n for n in lst1 if n % 2 == 0]
    if len(even_nums) == len(lst1):  # if lst1 is already all even, no need to exchange
        return "YES"
    for n in lst2:
        if n % 2 == 0 and len(even_nums) < len(lst1):  # if lst1 isn't all even yet, add even nums from lst2
            even_nums.append(n)
    if len(even_nums) == len(lst1):  # if lst1 is now all even, return "YES"
        return "YES"
    else:
        return "NO"
