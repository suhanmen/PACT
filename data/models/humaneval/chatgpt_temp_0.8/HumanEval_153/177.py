def Strongest_Extension(class_name, extensions):
    max_strength = None
    strongest_ext = None
    for ext in extensions:
        cap_count = sum(1 for ch in ext if ch.isupper())
        sm_count = sum(1 for ch in ext if ch.islower())
        strength = cap_count - sm_count
        if max_strength is None or strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    return class_name + '.' + strongest_ext
