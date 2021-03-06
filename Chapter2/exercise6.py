from pylab import*
import math
x=[0]
y=[0]
v_x=[]
v_y=[]
g=[]
T=[]
theta=float(raw_input('Please enter the firing angle:'))
v_0=float(raw_input('Please enter the initial speed:'))
dt=float(raw_input('Please enter the time steps:'))
g_0=float(raw_input('Please enter the value of the g:'))
k=float(raw_input('Please enter the value of B_2/m:'))
T=float(raw_input('Please enter the sea level temperature:'))
g.append(g_0)
v_x.append(v_0*math.cos(theta*math.pi/180))
v_y.append(v_0*math.sin(theta*math.pi/180))
while True:
    x.append(x[-1]+v_x[-1]*dt)
    y.append(y[-1]+v_y[-1]*dt)
    v_x.append(v_x[-1]-k*((1-0.0065*y[-1]/T)**2.5)*((v_x[-1]**2+v_y[-1]**2)**0.5)*v_x[-1]*dt)
    v_y.append(v_y[-1]-k*((1-0.0065*y[-1]/T)**2.5)*((v_x[-1]**2+v_y[-1]**2)**0.5)*v_y[-1]*dt-g[-1]*dt)
    g.append(((6400000/(6400000+y[-1]))**2)*g_0)
    if y[-1]<0:
        break
    print x[-1],y[-1]

plot(x,y,'-',color='blue')


ax=gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

xlabel('x(m)')
ylabel('y(m)')
title('Trajectory of cannon shell')

show()
