import pandas as pd  # Importing pandas for DataFrame manipulation
df = pd.DataFrame({
    'ID': [1, 2, 3],  # Column for unique ID
    'Math_2020': [85, 90, 78],  # Math scores for 2020
    'Math_2021': [88, 92, 80],  # Math scores for 2021
    'Science_2020': [89, 93, 82],  # Science scores for 2020
    'Science_2021': [91, 95, 84]  # Science scores for 2021
})

print("Original DataFrame:")
print(df)
df_long = pd.wide_to_long(df,
                          stubnames=['Math', 'Science'],
                          i='ID',  # The identifier column
                          j='Year',
                          sep='_',
                          suffix=r'\d+')  # Raw string for the suffix pattern: \d+ means match one or more digits

print("\nReshaped DataFrame (Long format):")
print(df_long)
