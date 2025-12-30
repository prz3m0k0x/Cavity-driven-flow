from methods.discretization.finite_differences import (
    central_difference_x, central_difference_y,
    backward_difference_x, backward_difference_y
)
import numpy as np

def compute_tentative_velocity(u, v, nu, dx, dy, dt,
                               scheme_first="backward",
                               scheme_second="central"):
    """
    Compute tentative velocity fields u*, v* using separate schemes
    for 1st and 2nd derivatives.

    Parameters
    ----------
    u, v : 2D ndarray
        Velocity fields
    nu : float
        Kinematic viscosity
    dx, dy : float
        Grid spacing
    dt : float
        Time step
    scheme_first : str
        "central" or "backward" for first derivatives (advection)
    scheme_second : str
        "central" or "backward" for second derivatives (diffusion)

    Returns
    -------
    u_star, v_star : ndarray
        Tentative velocity fields
    """

    # Select first derivative scheme
    if scheme_first == "central":
        dudx = central_difference_x(u, dx)
        dudy = central_difference_y(u, dy)
        dvdx = central_difference_x(v, dx)
        dvdy = central_difference_y(v, dy)
    elif scheme_first == "backward":
        dudx = backward_difference_x(u, dx)
        dudy = backward_difference_y(u, dy)
        dvdx = backward_difference_x(v, dx)
        dvdy = backward_difference_y(v, dy)
    else:
        raise ValueError("scheme_first must be 'central' or 'backward'")

    # Select second derivative scheme
    if scheme_second == "central":
        d2udx2 = central_difference_x(dudx, dx)
        d2udy2 = central_difference_y(dudy, dy)
        d2vdx2 = central_difference_x(dvdx, dx)
        d2vdy2 = central_difference_y(dvdy, dy)
    elif scheme_second == "backward":
        d2udx2 = backward_difference_x(dudx, dx)
        d2udy2 = backward_difference_y(dudy, dy)
        d2vdx2 = backward_difference_x(dvdx, dx)
        d2vdy2 = backward_difference_y(dvdy, dy)
    else:
        raise ValueError("scheme_second must be 'central' or 'backward'")

    # Tentative velocity update
    u_star = u + dt * (-u*dudx - v*dudy + nu*(d2udx2 + d2udy2))
    v_star = v + dt * (-u*dvdx - v*dvdy + nu*(d2vdx2 + d2vdy2))

    return u_star, v_star