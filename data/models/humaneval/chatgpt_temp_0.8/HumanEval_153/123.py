def Strongest_Extension(class_name, extensions):
    strongest_ext = extensions[0]
    strongest_strength = (strongest_ext.count(strongest_ext.upper()) 
                          - strongest_ext.count(strongest_ext.lower()))
    for ext in extensions[1:]:
        strength = (ext.count(ext.upper()) - ext.count(ext.lower()))
        if strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = strength
    return f"{class_name}.{strongest_ext}"
