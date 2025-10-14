def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split encoded string into groups of 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # create empty list to hold decoded groups
    decoded_groups = []
    # iterate through each group and decode it
    for group in groups:
        # if group has 3 characters, cycle the characters back one position and append to decoded_groups
        if len(group) == 3:
            decoded_groups.append(group[-1] + group[0:2])
        # if group has 2 characters, append the two characters to decoded_groups
        elif len(group) == 2:
            decoded_groups.append(group)
        # if group has 1 character, ignore it
        else:
            pass
    # join the decoded_groups list into a decoded string
    decoded_string = ''.join(decoded_groups)
    return decoded_string
