def file_name_check(file_name):
    if not file_name:
        return 'No' # empty file name
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No' # invalid file name format (should contain exactly one dot)
    name_before_dot = name_parts[0]
    name_after_dot = name_parts[1]
    if not name_before_dot or not name_before_dot[0].isalpha():
        return 'No' # invalid file name format (should start with a letter from the latin alphabet)
    if name_after_dot not in ['txt', 'exe', 'dll']:
        return 'No' # invalid file name format (should have one of the specified extensions)
    digits_count = len([ch for ch in name_before_dot if ch.isdigit()])
    if digits_count > 3:
        return 'No' # invalid file name format (should not have more than three digits)
    return 'Yes' # valid file name
