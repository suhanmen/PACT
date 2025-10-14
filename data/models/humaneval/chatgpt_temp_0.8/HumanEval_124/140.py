def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False
    
    # Split the date string into month, day and year components
    date_components = date.split("-")
    if len(date_components) != 3:
        return False
    
    month, day, year = date_components
    
    # Check if the month is valid
    if not (month.isdigit() and 1 <= int(month) <= 12):
        return False
    
    # Check if the day is valid based on the month
    if month in ["01", "03", "05", "07", "08", "10", "12"]:
        max_day = 31
    elif month in ["04", "06", "09", "11"]:
        max_day = 30
    elif month == "02":
        # Check if the year is a leap year
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
            max_day = 29
        else:
            max_day = 28
    else:
        return False
    
    if not (day.isdigit() and 1 <= int(day) <= max_day):
        return False
    
    # Check if the year is valid
    if not (year.isdigit() a
