def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')
    strongest_ext = ''
    
    for ext in extensions:
        cap_count = sum(1 for c in ext if c.isupper())
        sm_count = sum(1 for c in ext if c.islower())
        strength = cap_count - sm_count
        
        if strength > max_strength:
            max_strength = strength
            strongest_ext = ext
    
    return class_name + '.' + strongest_ext
