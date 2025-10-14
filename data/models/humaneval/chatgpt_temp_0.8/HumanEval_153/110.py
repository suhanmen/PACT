def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_ext = ''
    for ext in extensions:
        cap_count = sum(1 for letter in ext if letter.isupper())
        sm_count = sum(1 for letter in ext if letter.islower())
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    return f"{class_name}.{strongest_ext}"
