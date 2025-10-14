"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""



def two_unique_nums(list_of_nums):
    num_count = {}
    for num in list_of_nums:
        num_count[num] = num_count.get(num, 0) + 1
    unique_nums = [num for num, count in num_count.items() if count == 1]
    return unique_nums

# Example usage
# unique_list = two_unique_nums([1,2,3,2,3,4,5])
# print(unique_list)  # Output: [1, 4, 5]
