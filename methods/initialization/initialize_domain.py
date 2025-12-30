# methods/initialization/initialize_domain.py
import numpy as np

def create_domain(domain):
    """
    Initialize computational domain and mesh.

    Parameters
    ----------
    domain : dict
        Must contain 'nx', 'ny', 'lx', 'ly'

    Returns
    -------
    dict
        Contains 'nx', 'ny', 'lx', 'ly', 'dx', 'dy', 'x', 'y'
    """
    nx = domain["nx"]
    ny = domain["ny"]
    lx = domain["lx"]
    ly = domain["ly"]

    dx = lx / (nx - 1)
    dy = ly / (ny - 1)

    x = np.linspace(0.0, lx, nx)
    y = np.linspace(0.0, ly, ny)

    return {
        "nx": nx,
        "ny": ny,
        "lx": lx,
        "ly": ly,
        "dx": dx,
        "dy": dy,
        "x": x,
        "y": y
    }