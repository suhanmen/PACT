"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""



def remove_length(input_string, k):
    words = input_string.split()
    filtered_words = [word for word in words if len(word) != k]
    return ' '.join(filtered_words)

assert remove_length('The person is most value tet', 3) == 'person is most value'
