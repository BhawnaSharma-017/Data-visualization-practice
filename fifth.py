# Pie charts
import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,10,6,9]
working = [7,8,6,2,4]
eating = [2,3,4,1,5]
playing = [8,5,7,9,13]

slices = [7,2,2,13]
activities = ['sleeping' , 'eating' , 'working' , 'playing']
cols = ['c' , 'm' , 'r' , 'k']

plt.pie(slices,labels = activities , colors = cols , startangle = 90)
 
plt.xlabel('Input Chart')
plt.ylabel('Output Chart')
plt.title('Pie Chart')

plt.legend()
plt.show()