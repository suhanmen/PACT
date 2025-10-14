def Strongest_Extension(class_name, extensions):
    strongest_ext = extensions[0]
    strongest_strength = strength(extensions[0])
    for ext in extensions[1:]:
        ext_strength = strength(ext)
        if ext_strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = ext_strength
    return f"{class_name}.{strongest_ext}"
    
