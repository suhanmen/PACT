Here is the completed code snippet:

```python
def filter_data(students, min_height, min_weight):
    filtered_students = {}
    for name, (height, weight) in students.items():
        if height > min_height and weight > min_weight:
            filtered_students[name] = (height, weight)
    return filtered_students

assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}, 6.0, 70) == {'Cierra Vega': (6.2, 70)}
```

The `filter_data` function takes in a dictionary `students` with student names as keys and tuples of float values `(student_height, student_weight)` as values. It also takes in `min_height` and `min_weight` as the minimum height and weight values.

The function iterates over each student in the `students` dictionary and checks if their height and weight are both above the minimum values. If they are, the student is added to the `filtered_students` dictionary.

Finally, the function returns the `filtered_students` dictionary.

The provided assert statement tests the function with a sample input and checks if the output matches the expected result.