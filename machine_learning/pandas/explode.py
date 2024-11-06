import pandas as pd
data = {
    'ID': [1, 2, 3],
    'Fruits': [['Apple', 'Banana'], ['Orange', 'Grapes'], ['Mango']],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
exploded_df = df.explode('Fruits')
print("\nExploded DataFrame:")
print(exploded_df)
