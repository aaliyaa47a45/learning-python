# Projectile Motion Analysis Program

import math

print("Projectile Motion Calculator")

u = float(input("Enter initial velocity (m/s):"))
angle = float(input("Enter angle of projection (degrees):"))

theta = math.radian(angle)
g=9.8

range_proj = (u**2*math.sin(2*theta))/g
max_height = (u**2*(math.sin(theta))**2)/(2*g)
time_of_flight = (2*u*math.sin(theta))/g

print("\n--- Results---")
print("Range=",round(range_proj,2),"meters")
print("Maximum Height=",round(max_height,2),"meters")
print("Time of Flight=",round(time_of_flight,2),"seconds")

if angle==45:
    print("This angle gives maximum range.")
elif angle<45:
    print("Increasing angle will increase range.")
else:
    print("Decreasing angle will increase range.")
