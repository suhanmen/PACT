def order_by_points(nums):
    # Define a helper function to calculate the sum of digits for a given number
    def sum_digits(n):
        return sum(int(d) for d in str(abs(n)))

    # Use the key parameter of the sorted function to sort by sum of digits and index
    return sorted(nums, key=lambda n: (sum_digits(n), nums.index(n)))
