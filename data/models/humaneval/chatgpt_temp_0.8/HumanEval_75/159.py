def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    nums = []
    for i in range(2, a):
        if a % i == 0:
            nums.append(i)
    if len(nums) != 3:
        return False
    for num in nums:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
