def Strongest_Extension(class_name, extensions):
    strengths = {} # create a dictionary to store extension strengths
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper()) # count uppercase letters
        SM = sum(1 for c in extension if c.islower()) # count lowercase letters
        strengths[extension] = CAP - SM # calculate extension strength and add to dictionary
    strongest = max(strengths, key=strengths.get) # get the extension with the highest strength
    return f"{class_name}.{strongest}" # return the name of the strongest extension in the correct format
