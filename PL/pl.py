import numpy as np
import matplotlib.pyplot as plt

# z = 2x1 + 5x2
# x1 + x2 >= 4
# x1 >=2
# x1,x2 >= 0


z = lambda x1,x2 : 2*x1 + 5*x2

x1 = np.linspace(-5,10,2000)
x2 = np.linspace(-5,10,2000)

# x1 + x2 >= 4
y1 = 4 - x1


# Plot
# Axis

# Plot restrictions

plt.axvline(0.0, color = "black",label = "$x_1,x_2 \geq 0$")
plt.axhline(0.0, color = "black")
plt.plot(x,y1,color = "red",label = "$x_1 + x_2 \geq 4$")
plt.axvline(2.0, color = "blue",label = "$x_1 \geq 2")

# Feasible region
plt.fill_between(x1,
                np.maximum(25 - (1.5*x_1), (2*(x_1))),
                np.minimum(25 - (1.5*x_1), 8), 
                where=x1 >= 2,
color='green', alpha=0.25)



# Plot settings
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.legend()
plt.axis("on")

plt.xlim(0,5)
plt.ylim(0,5)
plt.show()
