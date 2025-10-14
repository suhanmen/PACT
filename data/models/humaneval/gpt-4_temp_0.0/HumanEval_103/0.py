# CANNOT PARSE
def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        total = 0
        count = 0
        for i in range(n, m+1):
            total += i
            count += 1
        average = round(total / count)
        return bin(average)

# Test cases
print(rounded_avg(1, 5))  # "0b11"
print(rounded_avg(7, 5))  # -1
print(rounded_avg(10, 20))  # "0b1111"
print(rounded_avg(20, 33))  # "0b11010"