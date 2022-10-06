def get_formatted_name(first_name, last_name, middle_name=''):
    # specifying a default value for middle_name incase no middle name is provided
    # generate fully formatted name
    if middle_name:
        full_name = (f"{first_name} {middle_name} {last_name}")
    else:
        full_name = (f"{first_name} {last_name}")
    return full_name.title()
