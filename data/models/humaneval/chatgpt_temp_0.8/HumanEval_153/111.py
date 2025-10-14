def Strongest_Extension(class_name, extensions):
    max_strength = None
    strongest_extension = None
    for extension in extensions:
        cap = 0
        sm = 0
        for c in extension:
            if c.isupper():
                cap += 1
            elif c.islower():
                sm += 1
        strength = cap - sm
        if max_strength == None or strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return class_name + '.' + strongest_extension
