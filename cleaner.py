def filter_nondigits(data: list) -> list:
    """
    Filters out strings that contain non-digit characters, and converts the remaining 
    valid strings into integers.

    Args:
    data (list): A list of items to filter.

    Returns:
    list: A new list containing integers from valid strings.
    """
    filtered_data = []

    for item in data:
        item = item.strip()
        if item.isdigit():
            filtered_data.append(float(item))
        
    return filtered_data
