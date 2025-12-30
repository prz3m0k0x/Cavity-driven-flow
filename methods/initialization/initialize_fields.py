"""
Docstring for methods.bc
This file creates the boundary conditions velocity field based on the
information passed to boundary_conditions.py.
It is important to use proper naming of boundary conditions
"""

def apply_velocity_bc(u, v, bc):
    ny, nx = u.shape

    for wall, spec in bc.items():
        wall_type = spec["type"]

        if wall_type == "stationary_wall":
            u_val, v_val = 0.0, 0.0

        elif wall_type == "moving_wall":
            try:
                u_val, v_val = spec["velocity"]
            except (KeyError, ValueError):
                raise ValueError(
                    f"Moving wall '{wall}' must define velocity = [u, v]"
                )

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