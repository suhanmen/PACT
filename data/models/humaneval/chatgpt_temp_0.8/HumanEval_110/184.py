def exchange(lst1, lst2):
    even_nums = [num for num in lst1 if num % 2 == 0]
    odd_nums = [num for num in lst1 if num % 2 != 0]
    if len(odd_nums) > len(lst2):
        return "NO"
    else:
        diff = len(lst2) - len(odd_nums)
        for num in lst2:
            if num % 2 == 0 and diff > 0:
                diff -= 1
        if diff == 0:
            return "YES"
        else:
            return "NO"
