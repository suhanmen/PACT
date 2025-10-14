def Strongest_Extension(class_name, extensions):
    strongest_extension = extensions[0]
    strength = extensions_strength(extensions[0])
    for extension in extensions[1:]:
        current_strength = extensions_strength(extension)
        if current_strength > strength:
            strongest_extension = extension
            strength = current_strength
    return f"{class_name}.{strongest_extension}"
