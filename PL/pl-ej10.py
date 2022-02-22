import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import tikzplotlib

# min z = x1 - 2x2
# 3x1 + 4x2 = 12
# 2x1 - x2 <= 12
# x1,x2 >= 0


c = np.array([1,-2])
c = c/np.sqrt(np.sum(c**2))
print(c)

# Restr 1 outside region
# 3x1 + 4x2 = 12
x0_1 = np.linspace(-2,0,500) 
x0_2 = np.linspace(4,7,1000)

y1_1 = (12-3*x0_1)/4
y1_2 = (12-3*x0_2)/4

# Rest 1 region
x1 = np.linspace(0,4,1000)
y_reg = (12-3*x1)/4


# Restr 2
# 2x1 - x2 <= 12
x2 = np.linspace(-5,10,2000)
y2 = 2*x2 - 12

# Filling point
x_fill = np.linspace(-5,10,2000)
y_fill = (12-3*x_fill)/4


# Plot

# Plot restrictions

figure(figsize=(10,8))

plt.axvline(0.0, color = "black",label = "$x_1,x_2 \geq 0$")
plt.axhline(0.0, color = "black")
plt.plot(x0_1,y1_1,color = "tomato",label = "$3x1 + 4x2 = 12$")
plt.plot(x0_2,y1_2,color = "tomato")

plt.plot(x1,y_reg,color = "maroon", linestyle = "--", label = "Feasible region")
plt.plot(x2,y2,color = "teal",label="$2x1 - x2 \leq 12$")

# Feasible region

plt.fill_between(x_fill,
                np.maximum(np.zeros(len(x_fill)),2*x_fill - 12 ),
                10,
                where=x2 >= 0,
                color='cornflowerblue',
                 alpha=0.25)


# Plot -c
o = np.array([0,0])
plt.quiver(*o, -c[0], -c[1], units = 'xy', scale = 1 ,color = "burlywood", label = "$-c$")

# Plot points

xs = [0,4]
ys = [3,0]

plt.scatter(xs,ys,color = "black")


# Plot settings
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.legend()
plt.axis("on")

plt.xlim(-1,7)
plt.ylim(-2,7)

#plt.savefig("Ej10.pdf")
#plt.show()
tikzplotlib.clean_figure()
tikzplotlib.save("Ej10.tex")

