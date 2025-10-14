"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""



def is_Sub_Array(main_list, sub_list):
    sub_len = len(sub_list)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i+sub_len] == sub_list:
            return True
    return False

# Example usage:
# result = is_Sub_Array([1,4,3,5], [1,2])
# print(result)  # Output: False
