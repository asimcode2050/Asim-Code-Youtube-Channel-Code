import pandas as pd  # Import the pandas library for DataFrame manipulation
# First DataFrame with columns 'A' and 'B'
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
# Second DataFrame with columns 'A' and 'B'
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
# Third DataFrame with columns 'A' and 'B'
df3 = pd.DataFrame({'A': [9, 10], 'B': [11, 12]})
concatenated_df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(concatenated_df)  # Display the resulting concatenated DataFrame
