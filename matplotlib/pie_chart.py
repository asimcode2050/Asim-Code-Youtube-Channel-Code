import matplotlib.pyplot as plt
categories = ['Apples', 'Bananas', 'Cherries', 'Grapes']
values = [40, 30, 20, 10]
explode = (0.1, 0, 0, 0)
plt.pie(values,  # The values parameter tells the pie chart how large each slice should be.
        labels=categories,
        autopct='%1.1f%%',
        explode=explode,
        startangle=90,
        colors=['red', 'yellow', 'pink', 'purple'])
plt.axis('equal')
plt.title('Fruit Distribution')
plt.show()
