# methods/initialization/initialize_fields.py
"""
Field initialization and boundary condition application for lid-driven cavity flow.
"""

import numpy as np

def create_fields(nx, ny):
    """
    Initialize velocity and pressure fields.

    Parameters
    ----------
    nx : int
        Number of grid points in x-direction
    ny : int
        Number of grid points in y-direction

    Returns
    -------
    tuple
        u, v, p arrays of shape (ny, nx)
    """
    u = np.zeros((ny, nx))
    v = np.zeros((ny, nx))
    p = np.zeros((ny, nx))
    return u, v, p


def apply_velocity_bc(u, v, bc):
    """
    Apply velocity boundary conditions to u and v arrays.

    Parameters
    ----------
    u, v : ndarray
        Velocity arrays
    bc : dict
        Boundary condition dictionary. Example:
        {
            "top": {"type": "moving_wall", "velocity": [1.0, 0.0]},
            "bottom": {"type": "stationary_wall"},
            "left": {"type": "stationary_wall"},
            "right": {"type": "stationary_wall"}
        }

    Returns
    -------
    tuple
        Updated u, v arrays
    """
    ny, nx = u.shape

    for wall, spec in bc.items():
        wall_type = spec.get("type", "stationary_wall")

        if wall_type == "stationary_wall":
            u_val, v_val = 0.0, 0.0
        elif wall_type == "moving_wall":
            vel = spec.get("velocity")
            if not vel or len(vel) != 2:
                raise ValueError(f"Wall '{wall}' must have 'velocity'=[u,v]")
            u_val, v_val = vel
        else:
            raise ValueError(f"Unknown wall type: {wall_type}")

        if wall == "top":
            u[-1, :] = u_val
            v[-1, :] = v_val
        elif wall == "bottom":
            u[0, :] = u_val
            v[0, :] = v_val
        elif wall == "left":
            u[:, 0] = u_val
            v[:, 0] = v_val
        elif wall == "right":
            u[:, -1] = u_val
            v[:, -1] = v_val
        else:
            raise ValueError(f"Unknown wall location: {wall}")

    return u, v