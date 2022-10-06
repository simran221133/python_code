def get_city(city, country, population = ''):
    # specifying a default value for middle_name incase no middle name is provided
    # generate fully formatted city name
    if population:
        place_name = (f"{city}, {country} - population {population}")
    else:
        place_name = (f"{city}, {country}")
    return place_name.title()