"""
Pressure Poisson solver for incompressible Navier-Stokes.
Solves ∇²p = rhs using iterative Jacobi method (or Gauss-Seidel if modified).
"""

import numpy as np

def solve_pressure_Jacobi(p, rhs, dx, dy, tol=1e-6, max_iter=2000):
    """
    Solve pressure Poisson equation ∇²p = rhs using iterative Jacobi.

    Parameters
    ----------
    p : 2D ndarray
        Initial pressure guess (usually zeros)
    rhs : 2D ndarray
        Right-hand side of Poisson eqn: divergence of tentative velocity
    dx, dy : float
        Grid spacing
    tol : float
        Convergence tolerance
    max_iter : int
        Maximum number of iterations

    Returns
    -------
    p : 2D ndarray
        Pressure field satisfying Poisson eqn
    """

    ny, nx = p.shape
    p_new = p.copy()

    for it in range(max_iter):
        p_old = p_new.copy()

        # Interior points
        p_new[1:-1, 1:-1] = (
            (dy**2*(p_old[1:-1, 2:] + p_old[1:-1, :-2]) +
             dx**2*(p_old[2:, 1:-1] + p_old[:-2, 1:-1]) -
             dx**2 * dy**2 * rhs[1:-1, 1:-1])
            / (2*(dx**2 + dy**2))
        )

        # Boundary conditions: dp/dn = 0 (Neumann)
        p_new[:, 0] = p_new[:, 1]      # left
        p_new[:, -1] = p_new[:, -2]    # right
        p_new[0, :] = p_new[1, :]      # bottom
        p_new[-1, :] = p_new[-2, :]    # top

        # Check convergence
        if np.linalg.norm(p_new - p_old, ord=2) < tol:
            break

    return p_new

import numpy as np

def solve_pressure_Gauss_Seidel(p, rhs, dx, dy, tol=1e-6, max_iter=2000):
    """
    Solve pressure Poisson equation ∇²p = rhs using Gauss-Seidel iteration.

    Parameters
    ----------
    p : 2D ndarray
        Initial pressure guess
    rhs : 2D ndarray
        Right-hand side (divergence of tentative velocity)
    dx, dy : float
        Grid spacing
    tol : float
        Convergence tolerance
    max_iter : int
        Maximum number of iterations

    Returns
    -------
    p : 2D ndarray
        Pressure field
    """

    ny, nx = p.shape

    for it in range(max_iter):
        p_old = p.copy()  # for convergence check

        for i in range(1, ny-1):
            for j in range(1, nx-1):
                p[i, j] = (
                    dy**2 * (p[i, j+1] + p[i, j-1]) +
                    dx**2 * (p[i+1, j] + p[i-1, j]) -
                    dx**2 * dy**2 * rhs[i, j]
                ) / (2*(dx**2 + dy**2))

        # Boundary conditions (Neumann)
        p[:, 0] = p[:, 1]      # left
        p[:, -1] = p[:, -2]    # right
        p[0, :] = p[1, :]      # bottom
        p[-1, :] = p[-2, :]    # top

        # Check convergence
        if np.linalg.norm(p - p_old, ord=2) < tol:
            break

    return p