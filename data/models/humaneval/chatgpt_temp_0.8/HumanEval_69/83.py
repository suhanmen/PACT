def search(lst):
    # Create a dictionary with keys as integers and values as their frequency in the list lst.
    freq_dict = {i: lst.count(i) for i in set(lst)}

    # Iterate over all the keys in the dictionary.
    for key in freq_dict:
        # Check if the key is greater than zero and its frequency is greater than or equal to the key.
        if key > 0 and freq_dict[key] >= key:
            # Return the key as it satisfies the given conditions.
            return key
    
    # If no such key exists, return -1.
    return -1
