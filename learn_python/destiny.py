import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(loc=0, scale=1, size=1000)

sns.kdeplot(data,
            fill=True,
            color="blue", 
            alpha=0.6)
plt.title("Density Plot of Normally Distributed Data")
plt.xlabel("Data Points")
plt.ylabel("Density")
plt.show()


