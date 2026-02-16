# Stack plots 

import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,10,6,9]
working = [7,8,6,2,4]
eating = [2,3,4,1,5]
playing = [8,5,7,9,13]

# plt.stackplot(x , y,y,y,y,..   , colors = ['','','','','',...])
plt.stackplot(days , sleeping,eating,working,playing , colors = ['m' , 'c' , 'r' ,'k'])

# To identify which color point to which stack plot -  We make lines of those color and give labels
plt.plot([],[], color = 'm' , label = 'Sleeping' , linewidth = 5)
plt.plot([],[], color = 'c' , label = 'Working' , linewidth = 5)
plt.plot([],[], color = 'r' , label = 'Eating' , linewidth = 5)
plt.plot([],[], color = 'k' , label = 'Playing' , linewidth = 5)


plt.xlabel ('Input label')
plt.ylabel ('Output label')
plt.title('Stack plots')

plt.legend()
plt.show()