import numpy as np
from methods.initialization.initialize_fields import apply_velocity_bc, apply_pressure_bc
from methods.pressure_poisson import solve_pressure_poisson
from methods.initialization.initialize_domain import initialize_domain, initialize_fields


def solve_cavity(domain, fluid, bc):

    x, y, dx, dy = initialize_domain(domain)

    nx = domain["nx"]
    ny = domain["ny"]

    u, v, p = initialize_fields(nx, ny)