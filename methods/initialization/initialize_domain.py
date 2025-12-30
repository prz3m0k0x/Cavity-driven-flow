import numpy as np


def initialize_domain(domain):
    nx = domain["nx"]
    ny = domain["ny"]
    lx = domain["lx"]
    ly = domain["ly"]

    dx = lx / (nx - 1)
    dy = ly / (ny - 1)

    x = np.linspace(0.0, lx, nx)
    y = np.linspace(0.0, ly, ny)

    return x, y, dx, dy


def initialize_fields(nx, ny):
    u = np.zeros((ny, nx))
    v = np.zeros((ny, nx))
    p = np.zeros((ny, nx))

    return u, v, p