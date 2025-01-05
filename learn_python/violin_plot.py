import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
np.random.seed(10)
category_1 = np.random.normal(loc=0, scale=1, size=100)
category_2 = np.random.normal(loc=1, scale=2, size=100)
category_3 = np.random.normal(loc=-1, scale=1.5, size=100)
data = pd.DataFrame({
    'Category 1': category_1,
    'Category 2': category_2,
    'Category 3': category_3
})
data_long = pd.melt(data, var_name='Category', value_name='Value')
plt.figure(figsize=(8, 6))
sns.violinplot(x='Category', y='Value', data=data_long)
plt.title('Violin Plot Example')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
