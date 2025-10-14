def valid_date(date):
    # Check if date string is not empty
    if not date:
        return False

    # Split the date into its components
    components = date.split("-")

    # Check if the date is in the format mm-dd-yyyy
    if len(components) != 3:
        return False

    # Check if all components are integers
    try:
        month = int(components[0])
        day = int(components[1])
        year = int(components[2])
    except ValueError:
        return False

    # Check if month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Check if day is valid for the given month and year
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # Leap year
            if day < 1 or day > 29:
                return False
        else:
            
