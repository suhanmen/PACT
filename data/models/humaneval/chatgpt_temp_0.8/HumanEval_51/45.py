def remove_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return ''.join([char for char in text if char not in vowels])
