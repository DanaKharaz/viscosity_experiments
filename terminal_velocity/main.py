# -*- coding: utf-8 -*-
"""
Graphs the metal bead's velocity as a function of time.
Gives the hyperbolic tangent equation describing the relationship.
Additionally, specifies the determined terminal velocity.
Can be used for each trial (1-10), for each concentration (0, 20, ..., 200 g).
"""

import matplotlib.pyplot
import numpy
import scipy.optimize

mass = int(input("Amount of sugar in grams: "))
if mass != 0 and mass != 20 and mass != 40 and mass != 60 and mass != 80 and mass != 100 and mass != 120 and mass != 140 and mass != 160 and mass != 180 and mass != 200:
  print("Invalid mass")
  quit()
trial = int(input("Trial number (1-10): "))
if trial < 1 or trial > 10:
  print("Number out of range")
  quit()
file = str(mass) + "g/" + str(trial)
title = str(mass) + " grams, trial #" + str(trial) + ", Velocity vs. Time"

#specify the equation
def function(t, a, b, c):
  return a * numpy.tanh(b * (t - c))  

array = numpy.loadtxt((file + ".txt"), delimiter = ",")
t = array[:,0]
v = array[:,1]

#determine the fitting curve/equation
params, c = scipy.optimize.curve_fit(function, t, v)
print("Terminal velocity: ", params[0])
if (params[2] < 0):
  print("Line equation: v = ", params[0], " * tanh(", params[1], " * ( t + ", -params[2], "))")
else:
  print("Line equation: v = ", params[0], " * tanh(", params[1], " * ( t - ", params[2], "))")

#graph the line of best fit
matplotlib.pyplot.plot(t, function(t, *params), 'ko-', linewidth='1', markersize='3', label = "Line of best fit")

#plot datapoints
matplotlib.pyplot.plot(t, v, ".", color="r", label = "Data")

#display the graph
matplotlib.pyplot.title(title)
matplotlib.pyplot.grid(True)
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.ylabel('Velocity')
matplotlib.pyplot.legend()
matplotlib.pyplot.savefig(file + ".png")
matplotlib.pyplot.show()