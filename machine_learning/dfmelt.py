import pandas as pd  # Importing pandas for DataFrame manipulation
df = pd.DataFrame({
    'ID': [1, 2, 3],    # Column for ID values
    'Math': [88, 92, 85],  # Column for Math scores
    'Science': [90, 93, 87],  # Column for Science scores
    'English': [85, 88, 90]   # Column for English scores
})

print("Original DataFrame:")
print(df)
df_long = pd.melt(df, id_vars=['ID'], value_vars=['Math', 'Science', 'English'],
                  var_name='Subject', value_name='Score')
print("\nReshaped DataFrame (Long format):")
print(df_long)
