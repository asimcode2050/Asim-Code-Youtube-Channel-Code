import pandas as pd  # Importing the pandas library to work with DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],  # Column 'A' with 4 values
    'B': ['B0', 'B1', 'B2', 'B3'],  # Column 'B' with 4 values
}, index=['K0', 'K1', 'K2', 'K3'])  # Setting custom index for df1


df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],  # Column 'C' with 4 values
    'D': ['D0', 'D1', 'D2', 'D3'],  # Column 'D' with 4 values
}, index=['K0', 'K1', 'K2', 'K3'])  # Setting custom index for df2

result = df1.join(df2)  # This will join df1 and df2 by their index (default)
print(result)  # Printing the joined DataFrame
