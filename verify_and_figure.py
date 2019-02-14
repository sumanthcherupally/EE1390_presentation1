import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,-7])
y = np.array([0,1])
r = np.array([1,7])
phi = np.linspace(0.0,2*np.pi,100)
na=np.newaxis
x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])

plt.xlim(-15,2)
plt.ylim(-7,9)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(0,1,'o')
plt.text(0,1,"Intersection Point (0,1)",horizontalalignment='right',verticalalignment='bottom')
plt.plot(x_line,y_line,'-')

P=np.array([0,1])
u1=np.array([0,0])
u2=np.array([1,-1])

dotproduct = np.dot((P.T+u1.T),(P+u2))
print("dotproduct of the directional vectors of two tangents drawn at the point of intersection = %d " %dotproduct)
if dotproduct==0:
	print('As dotproduct equals to zero the two circles intersect orthogonally')
else:
	print('The two circles does not intersect orthogonally ')



O=np.array([0,0])
Q=np.array([1,1])
lamb=np.linspace(-4,4,1000)
t1=np.zeros((2,1000))
t2=np.zeros((2,1000))
i=0
for i in range(1000):
    t1[:,i]=P+lamb[i]*(P-O)
    t2[:,i]=P+lamb[i]*(P-Q)



plt.plot(t1[0,:],t1[1,:])
plt.plot(t2[0,:],t2[1,:])
plt.grid()
plt.show()