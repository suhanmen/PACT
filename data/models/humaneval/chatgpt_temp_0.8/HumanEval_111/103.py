def histogram(test):
    count = {}
    test_list = test.split()
    for letter in test_list:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    max_count = max(count.values())
    result = {k:v for k,v in count.items() if v == max_count}
    return result
