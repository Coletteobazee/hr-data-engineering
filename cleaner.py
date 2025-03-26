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
        cleaned_item = item.strip()
        if cleaned_item.isdigit():
            filtered_data.append(int(cleaned_item))
        
    return filtered_data
