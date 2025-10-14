def count_nums(arr):
    count = 0
    for num in arr:
        num_str = str(num)
        num_sum = 0
        for i in range(len(num_str)):
            if num_str[i] == '-':
                num_sum -= int(num_str[i+1])
            else:
                num_sum += int(num_str[i])
        if num_sum > 0:
            count += 1
    return count
