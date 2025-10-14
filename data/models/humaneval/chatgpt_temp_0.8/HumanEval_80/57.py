def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """

    if len(s) < 3:  # if the string is less than 3 characters long, it can't be happy
        return False

    for i in range(len(s) - 2):  # iterate over all 3-letter sequences in the string
        if s[i] != s[i + 1] != s[i + 2] != s[i]:  # if all three letters are different, the string is happy
            return True

    return False  # if no happy sequence is found, the string is not happy
