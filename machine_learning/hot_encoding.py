import pandas as pd  # Import pandas for data manipulation
data = {'Color': ['Red', 'Green', 'Blue', 'Red', 'Green']}
df = pd.DataFrame(data)  # Convert the dictionary into a pandas DataFrame
df_encoded = pd.get_dummies(df, columns=['Color'])
print("Original DataFrame:")
print(df)
print("\nOne-Hot Encoded DataFrame:")
print(df_encoded)
