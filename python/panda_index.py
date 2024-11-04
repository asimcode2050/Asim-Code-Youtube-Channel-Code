# Place DataFrame data in one unique index in pandas
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
    'Age': [25, 30, 35, 40, 22, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df_unique = df.drop_duplicates(subset='Name')
print("\nDataFrame after removing duplicates:")
print(df_unique)

df_indexed = df_unique.set_index('Name')
print("\nDataFrame with 'Name' as index:")
print(df_indexed)

if not df_indexed.index.is_unique:
    print("\nIndex is not unique. Consider removing duplicates.")
else:
    print("\nIndex is unique.")

