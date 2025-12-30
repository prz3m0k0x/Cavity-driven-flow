# run.py
"""
Main script to run the lid-driven cavity solver
using configs from the config directory.
"""

from config.domain import domain
from config.boundary_conditions import BC
from config.fluid_properties import fluid

from methods.solver import solve_cavity
import matplotlib.pyplot as plt

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
    save_interval=50
)

#Plot final u-velocity
u = results["u"]
x, y = results["x"], results["y"]

plt.figure(figsize=(6,5))
plt.contourf(x, y, u, levels=50, cmap="jet")
plt.colorbar(label="u-velocity")
plt.xlabel("x")
plt.ylabel("y")
plt.title("u-velocity at final time")
plt.show()
