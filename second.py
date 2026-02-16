# Bar charts and Histograms

import matplotlib.pyplot as plt

# # Bar charts 
# x1= [2,4,6,8,10]
# y1= [1,3,5,7,9]
# plt.bar(x1,y1,label = 'Bar1' , color = 'pink')

# x2 = [3,5,7,9,1]
# y2 = [2,4,6,8,10]
# plt.bar(x2,y2 , label = 'Bar2' ,color = 'black')

# plt.xlabel('Input')
# plt.ylabel('Output')
# plt.title('Bar Graph')
# plt.legend()
# plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# Histograms
population_ages = [10,12,15,17,19,22,26,34,45,65,75,89,99,110,80,75,65,54,44,43,32,21]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar' , rwidth = 0.8)

plt.xlabel('Input number')
plt.ylabel('Output number')
plt.title('Histogram')
plt.legend()

plt.show()