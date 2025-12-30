"""
Docstring for config.domain
In this file the geometry is speicfied. Currently, only rectangular
shapes are supported.

nx and ny provide number of cells grid in given direciton
lx and ly specify the lenght of the domain in given direction
courant is a CFL number, which should be entered by user. It should always fall below 1.0 for stability reasons.
nt specifies number of timesteps, which are calculated from courant number as follows:
nt = lx / nx * courant / |U_boundary|
where |U_boundary| is the velocity magnitude at the boundary
"""

domain = {
    "nx": 41,
    "ny": 41,
    "lx": 0.2,
    "ly": 0.2,
    "courant": 0.05,
    "nt": 500
}