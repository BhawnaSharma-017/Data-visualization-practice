# import matplotlib.pyplot as plt 

# x1 = [1,2,3]
# y1 = [4,5,6]
# plt.plot(x1,y1 , label = 'First Line')

# x2 = [7,8,9]
# y2 = [6,3,2]
# plt.plot(x2,y2 , label = 'Second Line')

# plt.xlabel('Number graph')
# plt.ylabel('Output numbers')

# plt.title('Interesting Graph')
# plt.legend()

# plt.show()

import matplotlib.pyplot as plt

x1 = [2,4,6,3,2]
y1 = [4,6,2,7,4]

x2 = [4,6,8,5,8]
y2 = [8,6,3,8,9]

plt.plot(x1,y1,label = '1_data')
plt.plot(x2,y2,label = '2_data')

plt.xlabel("One side")
plt.ylabel('Other side')
plt.title("Learning")

plt.legend()
plt.show()