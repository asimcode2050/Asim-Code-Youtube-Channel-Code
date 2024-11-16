import pandas as pd
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Series:")
print(series)
custom_index = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(data, index=custom_index)
print("\nSeries with custom index:")
print(series_with_index)
print("\nElement with index 'c':")
print(series_with_index['c'])
print("\nElements with index 'b' and 'd':")
print(series_with_index[['b', 'd']])
print("\nSeries after multiplying each element by 2:")
print(series_with_index * 2)
print("\nCheck if 'a' is in the index:")
print('a' in series_with_index)
print("\nElements greater than 30:")
print(series_with_index[series_with_index > 30])


def custom_function(x):
    return x ** 2


print("\nSeries after applying custom function (square of each element):")
print(series_with_index.apply(custom_function))
series2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
combined_series = series_with_index + series2
print("\nCombined Series (element-wise addition):")
print(combined_series)
print("\nHandling missing values by filling NaN with 0:")
print(combined_series.fillna(0))
