python
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for char in text:
        if char not in vowels:
            result.append(char)
    return ''.join(result)
