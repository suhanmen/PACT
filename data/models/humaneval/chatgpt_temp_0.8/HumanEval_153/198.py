def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    strongest_strength = sum(1 for c in strongest_extension if c.isupper()) - sum(1 for c in strongest_extension if c.islower())
    for extension in extensions[1:]:
        extension_strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        if extension_strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = extension_strength
    return class_name + '.' + strongest_extension
