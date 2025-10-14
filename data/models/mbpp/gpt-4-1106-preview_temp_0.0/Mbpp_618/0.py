"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""



def div_list(list1, list2):
    try:
        return [a / b for a, b in zip(list1, list2)]
    except ZeroDivisionError:
        print('Error: Division by zero encountered.')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

# Example usage:
# result = div_list([4,5,6],[1, 2, 3])
# print(result)  # Output: [4.0, 2.5, 2.0]
