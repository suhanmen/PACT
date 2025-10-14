"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""



def right_insertion(sorted_list, value):
    left, right = 0, len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage:
# sorted_list = [1, 2, 4, 5]
# value = 6
# insertion_point = right_insertion(sorted_list, value)
# print(f'Insert {value} at index {insertion_point}')  # Output should be: Insert 6 at index 4
