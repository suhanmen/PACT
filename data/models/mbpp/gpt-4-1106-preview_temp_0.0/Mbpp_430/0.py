"""
Write a function to find the directrix of a parabola.
assert parabola_directrix(5,3,2)==-198
"""



def parabola_directrix(a, b, c):
    # The directrix of a parabola y=ax^2+bx+c is y = -D/4a
    # where D is the discriminant of the quadratic equation ax^2 + bx + c = 0
    # D = b^2 - 4ac
    D = b**2 - 4*a*c
    directrix_y = -D / (4*a)
    return directrix_y

# Example usage:
# directrix = parabola_directrix(5, 3, 2)
# print('Directrix:', directrix)

assert parabola_directrix(5, 3, 2) == -198
