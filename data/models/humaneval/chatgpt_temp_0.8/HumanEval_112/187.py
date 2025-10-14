def reverse_delete(s,c):
    s = ''.join([i for i in s if i not in c])
    return (s, s == s[::-1])
