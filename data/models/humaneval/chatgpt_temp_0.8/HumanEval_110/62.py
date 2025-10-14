def exchange(lst1, lst2):
    even_lst1 = [num for num in lst1 if num % 2 == 0]  # get even numbers from lst1
    even_count = len(even_lst1)  # count of even numbers in lst1
    odd_lst2 = [num for num in lst2 if num % 2 != 0]  # get odd numbers from lst2
    odd_count = len(odd_lst2)  # count of odd numbers in lst2
    
    if even_count > len(lst1)//2:  # if more than half of lst1 is already even
        return "YES"
    elif even_count + odd_count < len(lst1):  # if not enough odd numbers in lst2 to make all of lst1 even
        return "NO"
    else:
        return "YES"  # else we can exchange odd numbers from lst2 with any numbers from lst1
