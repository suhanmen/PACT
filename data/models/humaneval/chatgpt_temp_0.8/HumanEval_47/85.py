def median(l: list):
    """Return median of elements in the list l."""
    # Sort the list in ascending order
    sorted_list = sorted(l)
    # Get the length of the list
    n = len(sorted_list)
    # Check if the length of the list is odd or even
    if n % 2 == 0:
        # If the length of the list is even, get the two middle elements
        middle1 = sorted_list[n//2]
        middle2 = sorted_list[n//2 - 1]
        # Calculate the average of the two middle elements
        median = (middle1 + middle2) / 2
    else:
        # If the length of the list is odd, get the middle element
        median = sorted_list[n//2]
    return median
