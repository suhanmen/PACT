python
def can_arrange(arr):
    # iterate from the second element to the end
    for i in range(1, len(arr)):
        # check if the current element is smaller than the previous element
        if arr[i] < arr[i-1]:
            # return the index of the element that doesn't satisfy the condition
            return i-1
    # if no such element exists, return -1
    return -1
