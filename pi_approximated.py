import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, (ax1,ax2) = plt.subplots(1,2)
fig.set_size_inches(12, 5.5)

ax1.plot([0, 1],[0, 1],'w.')
ax2.plot([0,1000],[0,5],'w.')

circle = plt.Circle(( 0, 0 ), 1,fill=None)
ax1.add_patch(Rectangle((0, 0), 1, 1,fc="white",ec="blue"))
ax1.add_artist( circle )

import random          
i = 0                 
inD = 0   
while (i<2000): 
    i+=1
    x = random.random() 
    y = random.random() 
    if (x*x+y*y<=1):    
        inD+=1
        ax1.plot(x,y,'r+')
    else:
        ax1.plot(x,y,'y+')
    myPi=4*inD/i
    ax2.plot(i,myPi,'g.')


ax1.set_title("Pi approximated :%0.3f" %myPi)
ax2.set_xlabel("iterations")
ax2.set_ylabel("y")
ax2.set_title("f(i)=Pi")
plt.show()