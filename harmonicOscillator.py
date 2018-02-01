#system parameters
k = 20.
m = 3.
x0 = 1.
dt =0.01

#initial condition
x = 2.
v = 2.
a = 0.
t = 0.

#saving position and time in a file
saveFile = open('./position.dat', 'w')

for i in range(1000):
    f = -k*(x - x0)
    a = f/m
    v = v + a*dt
    x = x + v*dt
    t = i*dt
    saveFile.write("%5.4f %5.4f\n" % (t,x))
    #you can save as many quantities as you need, just remember to modify "%5.4f %5.4f\n"
    #print t , x

saveFile.close()

#reading positions file for ploting
pos = []
time = []
readFile=open('./position.dat', 'r')
if readFile.mode=='r' :
    for line in readFile:
        numbers_float = map(float, line.split())
        #print numbers_float[0], numbers_float[1]
        time = time + [numbers_float[0]]
        pos = pos + [numbers_float[1]]

#ploting
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(time,pos)
plt.grid()
plt.show()
fig.savefig('x-t.png')