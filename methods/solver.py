# solve_cavity.py
"""
2D Lid-Driven Cavity Solver (Modular)
Uses projection method with flexible finite difference schemes.
"""

import numpy as np
from methods.initialization.initialize_domain import create_domain
from methods.initialization.initialize_fields import create_fields, apply_velocity_bc
from methods.discretization.momentum import compute_tentative_velocity
from methods.discretization.poisson_pressure import solve_pressure_poisson


def solve_cavity(domain, fluid, bc, dt, t_final,
                 scheme_first="backward", scheme_second="central",
                 tol=1e-4, max_iter=500, save_interval=None):
    """
    Solve 2D lid-driven cavity flow using projection method.

    Parameters
    ----------
    domain : dict
        Must contain 'nx', 'ny', 'lx', 'ly'
    fluid : dict
        Must contain 'rho' and 'nu'
    bc : dict
        Boundary condition dictionary for velocity
    dt : float
        Time step
    t_final : float
        Final simulation time
    scheme_first : str
        Finite difference scheme for 1st derivatives ('central' or 'backward')
    scheme_second : str
        Finite difference scheme for 2nd derivatives ('central' or 'backward')
    tol : float
        Tolerance for pressure Poisson solver
    max_iter : int
        Maximum iterations for pressure Poisson solver
    save_interval : int or None
        If provided, save snapshots every N steps

    Returns
    -------
    results : dict
        u, v, p, x, y
    """

    # Initialize domain and mesh
    domain_data = create_domain(domain)
    nx, ny = domain_data["nx"], domain_data["ny"]
    dx, dy = domain_data["dx"], domain_data["dy"]
    x, y = domain_data["x"], domain_data["y"]

    #Initialize velocity and pressure fields
    u, v, p = create_fields(nx, ny)

    #Apply initial velocity BCs
    u, v = apply_velocity_bc(u, v, bc)

    #Time-step
    n_steps = int(t_final / dt)
    rho = fluid["rho"]
    nu = fluid["nu"]

    # Optional storage
    snapshots = []

    for step in range(n_steps):
        #Compute tentative velocity (u*, v*)
        u_star, v_star = compute_tentative_velocity(
            u, v, nu, dx, dy, dt,
            scheme_first=scheme_first,
            scheme_second=scheme_second
        )

        #Compute RHS of pressure Poisson equation
        rhs = np.zeros_like(p)
        rhs[1:-1, 1:-1] = (rho/dt) * (
            (u_star[1:-1, 2:] - u_star[1:-1, :-2]) / (2*dx) +
            (v_star[2:, 1:-1] - v_star[:-2, 1:-1]) / (2*dy)
        )

        #Solve pressure Poisson
        p = solve_pressure_poisson(p, rhs, dx, dy, tol=tol, max_iter=max_iter)

        #Update velocity using pressure gradient
        u[1:-1, 1:-1] = u_star[1:-1, 1:-1] - (dt/rho) * (p[1:-1, 2:] - p[1:-1, :-2]) / (2*dx)
        v[1:-1, 1:-1] = v_star[1:-1, 1:-1] - (dt/rho) * (p[2:, 1:-1] - p[:-2, 1:-1]) / (2*dy)

        #Apply velocity boundary conditions
        u, v = apply_velocity_bc(u, v, bc)

        #Optionally save snapshots
        if save_interval and step % save_interval == 0:
            snapshots.append({
                "u": u.copy(),
                "v": v.copy(),
                "p": p.copy(),
                "step": step
            })

    #Return final fields
    results = {
        "u": u,
        "v": v,
        "p": p,
        "x": x,
        "y": y,
        "snapshots": snapshots
    }
    return results