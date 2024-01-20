import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from random import random
from statistics import mean
fig, (ax1,ax2) = plt.subplots(1,2)
fig.set_size_inches(12, 5.5)

ax1.plot([0, 1],[0, 1],'w.')
ax2.plot([0,1000],[0,5],'w.')

circle = plt.Circle(( 0, 0 ), 1,fill=None)
ax1.add_patch(Rectangle((0, 0), 1, 1,fc="white",ec="blue"))
ax1.add_artist( circle )
l=[]
for t in range(500):
    i = 0                 
    inD = 0   
    while (i<3000): 
        i+=1
        x = random() 
        y = random() 
        if (x*x+y*y<=1):    
            inD+=1
            if(t==1):
                ax1.plot(x,y,'r+')
        else:
            if(t==1):
                ax1.plot(x,y,'y+')
        myPi=4*inD/i
        if(t==1):
            ax2.plot(i,myPi,'g.')
    l.append(myPi)

ax1.set_title("Pi approximated in test 1: %0.3f\nPi approximated after 500 tests: %0.3f\n-Visualisation for test 1:" %(myPi,mean(l)))
ax2.set_xlabel("iterations")
ax2.set_ylabel("y")
ax2.set_title("Convergence in test 1\nf(i)=Pi")
plt.show()