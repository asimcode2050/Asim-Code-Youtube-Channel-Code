import pandas as pd
df1 = pd.DataFrame({
    'January': [200, 300, 400],
    'February': [220, 330, 450]
}, index=['Product A', 'Product B', 'Product C'])


df2 = pd.DataFrame({
    'March': [250, 350, 470],
    'April': [270, 370, 500]
}, index=['Product A', 'Product B', 'Product C'])

df_sum = df1 + df2
df_diff = df1 - df2
df_prod = df1 * df2
df_div = df1 / df2
print("Original DataFrame 1:")
print(df1)
print("\nOriginal DataFrame 2:")
print(df2)
print("\nSum of DataFrame 1 and DataFrame 2:")
print(df_sum)
print("\nDifference of DataFrame 1 and DataFrame 2:")
print(df_diff)
print("\nProduct of DataFrame 1 and DataFrame 2:")
print(df_prod)
print("\nDivision of DataFrame 1 by DataFrame 2:")
print(df_div)
