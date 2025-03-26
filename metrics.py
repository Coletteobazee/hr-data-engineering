def average(data: list) -> float:
    """
    Calculate average value (mean) of the list.
    """
    if not data:
        return []
    
    total = 0

    for value in data:
        total += value
    average = total / len(data)    
    return round(average, 2)


def maximum(data: list) -> float:
    """
    Calculate the maximum value from the list.
    """
    if not data:
        return []
    
    max_value = data[0]

    for value in data:
        if value > max_value:
            max_value = value

    return float(max_value)


def variance(data: list) -> float:
    """
    Calculate the variance of the list.
    (calculate population variance)
    """
    if not data: 
        return []
    
    mean = average(data)
    squared_diffs = 0
    for value in data:
        squared_diffs += (value - mean) ** 2
    variance_value = squared_diffs / len(data)
    return round(variance_value, 2)


def standard_deviation(data: list) -> float:
    """
    Calculate the standard deviation of the data
    (calculate population standard deviation)
    """
    if not data: 
        return []
    
    var = variance(data)
    std_dev = var ** 0.5
    return round(std_dev, 2)
