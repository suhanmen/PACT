def exchange(lst1, lst2):
    even_nums = [n for n in lst1 if n % 2 == 0]
    odd_nums = [n for n in lst1 if n % 2 != 0]
    if len(odd_nums) != 0:
        return "NO"
    else:
        for num in lst2:
            if num % 2 == 0:
                lst1.append(num)
        even_nums2 = [n for n in lst1 if n % 2 == 0]
        if len(even_nums2) == len(lst1):
            return "YES"
        else:
            return "NO"
