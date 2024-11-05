import pandas as pd
series1 = pd.Series([10, 20, 30, 40, 50], name="Series 1")
series2 = pd.Series([1, 2, 3, 4, 5], name="Series 2")
sum_series = series1 + series2
difference_series = series1 - series2
product_series = series1 * series2
division_series = series1 / series2
print("Original Series 1:")
print(series1)
print("\nOriginal Series 2:")
print(series2)
print("\nSum of Series 1 and Series 2:")
print(sum_series)
print("\nDifference of Series 1 and Series 2:")
print(difference_series)
print("\nProduct of Series 1 and Series 2:")
print(product_series)
print("\nDivision of Series 1 by Series 2:")
print(division_series)
