"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""



def search(arr):
    # Initialize left and right pointers
    left, right = 0, len(arr) - 1

    # Binary search approach
    while left < right:
        mid = left + (right - left) // 2

        # Check if the mid is at the start of a pair
        if mid % 2 == 0:
            # If the next element is the same, the single element is on the right
            if arr[mid] == arr[mid + 1]:
                left = mid + 2
            else:
                right = mid
        else:
            # If the previous element is the same, the single element is on the right
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1

    # When left == right, we have found the single element
    return arr[left]

# Example usage
assert search([1,1,2,2,3]) == 3
