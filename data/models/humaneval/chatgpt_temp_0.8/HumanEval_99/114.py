# CANNOT PARSE CODE SNIPPET
def closest_integer(num_str):
    num = float(num_str)
    int_num = int(num)
    if num - int_num >= 0.5:
        return int_num + 1
    elif num - int_num <= -0.5:
        return int_num - 1
    else:
        return int_num
