def sort_even(l: list):
    even_list = l[::2] # Get the even-indexed values of l
    even_list.sort() # Sort the even-indexed values
    l_prime = l.copy() # Create a copy of the original list
    l_prime[::2] = even_list # Replace the even-indexed values of l_prime with the sorted even_list
    return l_prime
