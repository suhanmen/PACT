def sort_third(l: list):
    # Create a new list to store the sorted values
    sorted_values = []
    # Iterate over the indices of the input list
    for i in range(len(l)):
        # If the index is not divisible by 3, add the value from the input list to the new list
        if i % 3 != 0:
            sorted_values.append(l[i])
        # If the index is divisible by 3, add the value from the input list to a temporary list
        else:
            temp_list = [l[i]]
            # Keep adding values from the input list to the temporary list until we reach an index that is not divisible by 3 or the end of the list
            j = i + 1
            while j < len(l) and j % 3 == 0:
                temp_list.append(l[j])
                j += 1
            # Sort the temporary list and add its values to the new list
            temp_list.sort()
            sorted_values.extend(temp_list)
    # Return the new list
    return sorted_values
