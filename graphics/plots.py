import numpy as np
import matplotlib.pyplot as plt


def plot_fields(x, y, u, v, p, time=None, save=False, filename=None):
    """
    Plot velocity magnitude and pressure contours.

    Parameters
    ----------
    x, y : 1D arrays
        Grid coordinates
    u, v : 2D arrays
        Velocity components
    p : 2D array
        Pressure field
    time : float, optional
        Simulation time
    save : bool
        Save figure to file
    filename : str, optional
        Output filename
    """

    X, Y = np.meshgrid(x, y)
    speed = np.sqrt(u**2 + v**2)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Velocity magnitude
    cs1 = axes[0].contourf(X, Y, speed, levels=50, cmap="viridis")
    axes[0].set_title("Velocity magnitude")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    fig.colorbar(cs1, ax=axes[0])

    # Pressure
    cs2 = axes[1].contourf(X, Y, p, levels=50, cmap="coolwarm")
    axes[1].set_title("Pressure")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("y")
    fig.colorbar(cs2, ax=axes[1])

    if time is not None:
        fig.suptitle(f"Time = {time:.3f}")

    plt.tight_layout()

    if save:
        if filename is None:
            filename = "cavity_snapshot.png"
        plt.savefig(filename, dpi=300)

    plt.show()

def plot_velocity_vectors(x, y, u, v, stride=2, scale=None):
    """
    Plot velocity vector field using quiver.

    Parameters
    ----------
    x, y : 1D arrays
        Grid coordinates
    u, v : 2D arrays
        Velocity components
    stride : int
        Plot every `stride` grid point (for clarity)
    scale : float, optional
        Quiver scaling
    """

    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(6, 6))
    plt.quiver(
        X[::stride, ::stride],
        Y[::stride, ::stride],
        u[::stride, ::stride],
        v[::stride, ::stride],
        scale=scale
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Velocity vectors")
    plt.axis("equal")
    plt.show()

def plot_streamlines(x, y, u, v, density=1.5):
    """
    Plot streamlines of velocity field.

    Parameters
    ----------
    x, y : 1D arrays
        Grid coordinates
    u, v : 2D arrays
        Velocity components
    density : float
        Controls streamline density
    """

    X, Y = np.meshgrid(x, y)
    speed = np.sqrt(u**2 + v**2)

    plt.figure(figsize=(6, 6))
    plt.streamplot(
        X, Y, u, v,
        color=speed,
        cmap="viridis",
        density=density,
        linewidth=1
    )

    plt.colorbar(label="Velocity magnitude")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Streamlines")
    plt.axis("equal")
    plt.show()