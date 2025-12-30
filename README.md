# Cavity-driven-flow

This repository contains my project on primitive CFD solver. It contains time-marching scheme with pressure - momentum coupled scheme. 
Currently it supports central and backward difference scheme for calcualting gradients; Jacobi and Gauss-Seidel method for solving Poisson equation for pressure - although GS scheme is paifuly slow with python loops.

To use the solver open the \config and:
1. Setup your boundary conditions.
  Currently two types of BC are involved - stationary and moving wall.
  To setup moving wall in the dictionary contained in boundary_conditions.py file enter "moving_wall" for keyword "type". Then, for keyword "velocity" enter list containing elements of velocity vector of the wall.
  For stationary wall simply write "type" : "stationary_wall".
  Note that four walls have to be specified with corresponding keywords "left", "right", "top" and "bottom".
3. Setup fluid properties, for now just viscosity and density
4. Setup domain setting - nubmer of grid points in x and y direction, lenght of the domain bounds, Courant number and number of timesteps
5. Save files and run the run.py file in the main directory.

If there are troubles with convergence i suggest manipulating Courants number, timesteps and sizing of the grid.
You can use premade graphics module that provide velocity magnitude and pressure contours. Also animations are available to use.
To setup animation you must enter number of saves in the run.py file calling function solve_cavity(). To do so specity kwarg save_interval= to the value of your needs. Details are included in docstring.
Animations and contours are included in the run.py file

Further works would definietely include adding more stable schemes for gradients, as stability of solutions i currently the main issue.
