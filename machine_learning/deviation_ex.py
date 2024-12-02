
def calculate_standard_deviation(data):
    """
    This function calculates the standard deviation of a given dataset.
    Standard deviation is a measure of how much the values deviate from the mean.
    """
    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    standard_deviation = variance ** 0.5
    return standard_deviation


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = calculate_standard_deviation(data)
print(f"The standard deviation of the dataset is: {result}")
