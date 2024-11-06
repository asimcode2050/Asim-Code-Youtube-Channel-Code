import pandas as pd
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
grouped = df.groupby('Category')
result = grouped['Value'].sum()
print(result)
