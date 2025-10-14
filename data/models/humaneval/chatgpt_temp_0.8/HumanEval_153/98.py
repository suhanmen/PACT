def Strongest_Extension(class_name, extensions):
    strongest_extension_name = None
    strongest_extension_strength = None
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        current_extension_strength = cap_count - sm_count
        if strongest_extension_strength is None or current_extension_strength > strongest_extension_strength:
            strongest_extension_name = extension
            strongest_extension_strength = current_extension_strength
    return class_name + '.' + strongest_extension_name
