python
def odd_count(lst):
    result = []
    for s in lst:
        count = sum(int(d) % 2 == 1 for d in s)
        message = "the number of odd elements in the string {} of the input.".format(s)
        result.append(message.replace('{}', str(count)))
    return result
