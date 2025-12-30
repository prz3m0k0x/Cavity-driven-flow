# methods/discretization/finite_differences.py
"""
Finite difference operators for 2D arrays.
Supports central and backward difference schemes.
"""

import numpy as np

def central_difference_x(f, dx):
    """
    Compute del f/ del x using central differences for interior points.

    Parameters
    ----------
    f : 2D ndarray
        Field to differentiate
    dx : float
        Grid spacing in x

    Returns
    -------
    df_dx : 2D ndarray
        Array of same shape as f with derivative in x
    """
    df_dx = np.zeros_like(f)
    df_dx[:, 1:-1] = (f[:, 2:] - f[:, :-2]) / (2*dx)
    return df_dx

def central_difference_y(f, dy):
    """
    Compute del f/del y using central differences for interior points.
    """
    df_dy = np.zeros_like(f)
    df_dy[1:-1, :] = (f[2:, :] - f[:-2, :]) / (2*dy)
    return df_dy

def backward_difference_x(f, dx):
    """
    Compute del f/del x using backward differences.
    """
    df_dx = np.zeros_like(f)
    df_dx[:, 1:] = (f[:, 1:] - f[:, :-1]) / dx
    return df_dx

def backward_difference_y(f, dy):
    """
    Compute del f/del y using backward differences.
    """
    df_dy = np.zeros_like(f)
    df_dy[1:, :] = (f[1:, :] - f[:-1, :]) / dy
    return df_dy