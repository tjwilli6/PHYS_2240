import numpy as np
import matplotlib.pyplot as plt

def plot():
    for row in rlist:
        plt.scatter(row[0],row[1],c='blue')
        plt.ylim(0,10)
        plt.xlim(-1,50)

ri = np.array( [0,2,0] )
pi = np.array( [2.1,2.1,0] )
m = 0.15
g = 9.81
dt = 0.5

pnow = pi
rnow = ri

rlist = []
rlist.append(ri)
plot()
plt.show()
for i in range(5):
    Fnet = np.array( [0,-m*g,0] )
    pfuture = pnow + Fnet * dt
    vavg = pfuture / m
    rfuture = rnow + vavg * dt
    pnow = pfuture
    rnow = rfuture
    rlist.append(rnow)
    plot()
    plt.show()
