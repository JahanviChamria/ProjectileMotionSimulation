Web VPython 3.2
graph(width=400, height=250, background=color.white,  xtitle='<i>time</i>', ytitle='<i>velocity</i>')
xDots = gdots(color=color.green)
yDots = gdots(color=color.magenta)
ball=sphere(pos=vector(0,10,0), color=color.red, make_trail=True, trail_type="points",   interval=1)
ground=box(length=50, width=50, height=0.1, color=color.white, pos=vector(0,0,0))
scene.background=color.cyan
scene.center=vector(0,5,0)
scene.width=400
g=9.8
dt=0.08
vy=0
y=10
drag=0.1
t=0
x=0
while y > 0:
    rate(20)
    ay = -g+(drag*abs(vy)**2) # ay at beginning of interval
    ymid = y + vy*0.5*dt # y at middle of interval
    vymid = vy + ay*0.5*dt # vy at middle of interval
    aymid = -g # ay at middle of interval
    y += vymid * dt
    vy += aymid * dt
    t += dt
    x+=1
    ball.pos=vector(x,y,0)
    xDots.plot(t, vy)
print("Ball lands at t =", t, "seconds, with velocity", -vy, "m/s")
