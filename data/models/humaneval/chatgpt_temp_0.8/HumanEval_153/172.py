def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    for extension in extensions[1:]:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        extension_strength = cap_count - sm_count
        strongest_cap_count = sum(1 for c in strongest_extension if c.isupper())
        strongest_sm_count = sum(1 for c in strongest_extension if c.islower())
        strongest_strength = strongest_cap_count - strongest_sm_count
        if extension_strength > strongest_strength:
            strongest_extension = extension
        elif extension_strength == strongest_strength and extensions.index(extension) < extensions.index(strongest_extension):
            strongest_extension = extension
    return class_name + "." + strongest_extension
