def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_ext = None
    for ext in extensions:
        upper_count = sum(1 for letter in ext if letter.isupper())
        lower_count = sum(1 for letter in ext if letter.islower())
        strength = upper_count - lower_count
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    return f"{class_name}.{strongest_ext}"
