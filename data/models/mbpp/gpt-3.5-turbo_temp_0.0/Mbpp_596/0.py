import sys

def tuple_size(t):
    return sys.getsizeof(t)

assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))