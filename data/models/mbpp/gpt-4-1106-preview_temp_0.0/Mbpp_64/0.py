"""
Write a function to sort a list of tuples using the second value of each tuple.
assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""


def subject_marks(subjects):
    # Sort the list of tuples based on the second value (marks)
    return sorted(subjects, key=lambda x: x[1])

# Example usage:
# sorted_subjects = subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
# print(sorted_subjects)
