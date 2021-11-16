import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

best_fitnesses = np.array([])

# n = input("What size was n? ")
n = 100

# with open('00-20-56.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in reader:
#         print(row)
#         best_fitnesses = np.append(best_fitnesses,row)
#
# print(type(best_fitnesses[0]))
# best_fitnesses = best_fitnesses.astype(float)/float(n)
# print(type(best_fitnesses[0]))
# print(best_fitnesses)

with open('fitness-10-39-02.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:

        best_fitnesses = np.append(best_fitnesses,row[0].split(','))

print(best_fitnesses)

best_fitnesses = best_fitnesses.astype(np.float)

print(type(best_fitnesses[0]))
best_fitnesses = best_fitnesses.reshape(-1,10)
best_fitnesses = best_fitnesses/float(n)
print(best_fitnesses)



TWOPI = 2*np.pi

fig, ax = plt.subplots()

x = np.linspace(-5.12,5.12,100)
y = 10 + x**2 - (10*np.cos(2*np.pi*x))
l = plt.plot(x, y)

# plt.show()
# exit()

# just creates a tuple, basiclly an irrelavant function
# ax = plt.axis([0,TWOPI,-1,1])

xlist = [0] * n
ylist = [0] * n


redDot, = plt.plot(xlist, ylist, 'ro')
# redDot, = plt.plot([0], [0], 'ro')

# plt.show()
# # exit()

def objective(x):
    return 10 + x**2 - (10*np.cos(2*np.pi*x))

def animate(i):
    redDot.set_data(i, objective(i))
    return redDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=best_fitnesses, interval=10, blit=True, repeat=True)

plt.show()