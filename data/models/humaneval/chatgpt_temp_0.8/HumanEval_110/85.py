def exchange(lst1, lst2):
    even_nums = [num for num in lst1 if num % 2 == 0]
    odd_nums = [num for num in lst1 if num % 2 != 0]
    if len(odd_nums) > len(lst2):
        return "NO"
    else:
        remaining_nums = [num for num in lst2 if num % 2 == 0]
        if len(even_nums) + len(remaining_nums) >= len(lst1):
            return "YES"
        else:
            return "NO"
