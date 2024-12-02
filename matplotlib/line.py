import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 24, 19, 23, 25, 27, 28]
plt.plot(days,
         temperatures,
         color='blue',
         marker='o',
         linestyle='-',
         linewidth=2
         )
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (C)')
plt.title('Temperature Over a Week')
plt.show()
