# run.py
"""
Main script to run the lid-driven cavity solver
using configs from the config directory.
"""
import matplotlib.pyplot as plt

from config.domain import domain
from config.boundary_conditions import BC
from config.fluid_properties import fluid
from methods.solver import solve_cavity
from graphics.plots import plot_fields, plot_velocity_vectors, plot_streamlines
from graphics.animations import (
    animate_contours,
    animate_vectors
)



nx = domain["nx"]
ny = domain["ny"]
lx = domain["lx"]
ly = domain["ly"]

dx = lx / (nx - 1)
dy = ly / (ny - 1)

# Compute dt from Courant number
courant = domain.get("courant", 0.5)
# maximum velocity on moving walls
Umax = max(v["velocity"][0] for v in BC.values() if "velocity" in v) or 1.0
dt = courant * dx / Umax

# Simulation parameters
nt = domain.get("nt", 500)
t_final = dt * nt

# Run the solver
results = solve_cavity(
    domain,
    fluid,
    BC,
    dt=dt,
    t_final=t_final,
    scheme_first="backward",   # advection
    scheme_second="central",   # diffusion
    save_interval=1
)

#Plot final u-velocity
u = results["u"]
v = results["v"]
p = results["p"]
x, y = results["x"], results["y"]
t = t_final

#plot_fields(x, y, u, v, p, t)
#plot_velocity_vectors(x, y, u, v)
#plot_streamlines(x, y, u, v)

animate_contours(
    results["x"],
    results["y"],
    results["u_hist"],
    results["v_hist"],
    results["p_hist"]
)

animate_vectors(
    results["x"],
    results["y"],
    results["u_hist"],
    results["v_hist"],
    stride=4,
    save=False
)