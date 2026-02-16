# Scatter plots     -- show dots

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,3]
plt.scatter(x,y,label = 'skitscat' , color = 'k' , marker = 'o' , s= 25)


plt.xlabel('Input Label')
plt.ylabel('Output label')

plt.title('Scatter plots')
plt.legend()
plt.show()