def Strongest_Extension(class_name, extensions):
    strongest_ext = None
    strongest_strength = None
    
    for ext in extensions:
        cap_count = sum(1 for c in ext if c.isupper())
        sm_count = sum(1 for c in ext if c.islower())
        ext_strength = cap_count - sm_count
        
        if strongest_ext is None or ext_strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = ext_strength
    
    return class_name + '.' + strongest_ext
