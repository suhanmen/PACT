def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # using list comprehension to filter out vowels from the text
    filtered_text = [char for char in text if char not in vowels]
    # join the filtered_text list into a string and return
    return ''.join(filtered_text)

