# -*- coding: utf-8 -*-
"""
Graphs the solution's viscosity as a function of concentration.
Gives the exponential equation describing the relationship.
"""

import matplotlib.pyplot
import numpy
import scipy.optimize

#specify the equation
def function(x, a, b, c):
  return a * numpy.exp(b * x) + c

array = numpy.loadtxt("data.txt", delimiter = ",")
c = array[:,0]
v = array[:,1]

title = "points"

print("Should the curve be included? (yes/no)")
task = str(input())
if (task == "yes"):
  #determine the fitting curve/equation
  params, curve = scipy.optimize.curve_fit(function, c, v);
  print("Line equation: v = ", params[0], " * e^( ", params[1], " * c ) + ", params[2])
  
  #graph the line of best fit
  matplotlib.pyplot.plot(c, function(c, *params), 'k-', linewidth = '1', label = "Line of best fit")

  title = "curve"
elif (task != "no"):
  print("Invalid input")
  quit()

#error bars
x = [0, 0.00001111, 0.00001122, 0.00001094, 0.00001049, 0.00001000, 0.00000950, 0.00000903, 0.00000858, 0.00000816, 0.00000778]
y = [0.00664, 0.00560, 0.00658, 0.00643, 0.00730, 0.00633, 0.00612, 0.00843, 0.00997, 0.01183, 0.01158]
matplotlib.pyplot.errorbar(c, v, xerr = x, yerr = y, fmt = 'none', ecolor = 'purple', elinewidth = 1, capsize = 3)

#plot datapoints
matplotlib.pyplot.plot(c, v, ".", markersize = 8, color = "r", label = "Data")

#display the graph
matplotlib.pyplot.title("Viscosity vs. Concentration")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.xlabel('Concentration')
matplotlib.pyplot.ylabel('Viscosity')
matplotlib.pyplot.legend()
matplotlib.pyplot.savefig(title + ".png")
matplotlib.pyplot.show()