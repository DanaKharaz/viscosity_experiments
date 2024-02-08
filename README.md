# viscosity_experiments
This is a program to analyze and graph data for a physics experiment. Time of development: 02/2023

The goal of the experiment was to analyze how the concentration of sugar affects the viscosity of sugar-water solutions using Stokes' law. To analyze the recorded data, 2 programs were created:

1 - terminal_velocity

A metal bead was dropped into solutions of different concentrations and its' motion was recorded. The videos were analyzed with Tracker to see the variation of the bead's velocity with time. Then with matplotlib, the data was graphed. Then a hyperbolic tangent function was fit to the data to determine the bead's terminal velocity. The program then outputs the plot with the fitted curve and the determined equation (with the terminal velocity separately specified as well). The program asks for the needed concentration (0, 20, ..., 200 grams in solution) and trial number (1-10) to determine which part of the data to analyze.

2 - viscosity_vs_concentration

After further manipulation, the viscosity of each solution based on concentration was determined. This program then plots determined values specifying the error (with matplotlib). And, if asked by the user, fits an exponential curve through the data points and gives its equation to describe the possible relationship between viscosity and concentration of sugar-water solutions.
