import pandas as pd
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [30, 70, 32, 72]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
pivoted_df = df.pivot(index='Date', columns='City', values='Temperature')
print("\nPivoted DataFrame:")
print(pivoted_df)
