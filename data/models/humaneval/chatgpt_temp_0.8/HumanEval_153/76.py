def Strongest_Extension(class_name, extensions):
    strongest_ext = extensions[0]
    strongest_strength = (extensions[0].count(x.isupper()) - extensions[0].count(x.islower())) for x in extensions[0]
    for ext in extensions[1:]:
        ext_strength = (ext.count(x.isupper()) - ext.count(x.islower())) for x in ext
        if ext_strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = ext_strength
    return f"{class_name}.{strongest_ext}"
