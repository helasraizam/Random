import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

def f(x,y):
	return 2.0*x+y


# Main code starts here
fig=plt.figure()				# Create figure
ax=fig.gca(projection='3d')	# Be in 3d
plt.hold(True)				# So we can plot two plots on top of each other

# Start Surface Plot
X=np.arange(-10.0,10.0,1.0)
Y=np.arange(-10.0,10.0,1.0)
X,Y=np.meshgrid(X,Y)		# Make mesh
Z=f(X,Y)
G=f(X,Y)
N=G/G.max()
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.25,facecolors=cm.coolwarm(N),linewidth=0,antialiased=False,shade=False)

# Start Gradient Plot
cset = ax.contour(X, Y, Z, cmap=cm.coolwarm,alpha=.9)
ax.clabel(cset, fontsize=9, inline=1)

# Bottom (xy-plane) contour
cset = ax.contour(X, Y, Z, zdir='z', offset=-30, cmap=cm.coolwarm)
ax.clabel(cset,fontsize=9,inline=1)

# Labels
ax.set_title("Plot of f(x,y)=2x+y")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show plot
plt.show()						
