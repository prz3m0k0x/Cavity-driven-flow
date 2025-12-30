import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_contours(x, y, u_hist, v_hist, p_hist,
                     interval=50, save=False, filename="contours.mp4"):
    """
    Animate velocity magnitude and pressure contours.
    """

    X, Y = np.meshgrid(x, y)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    speed0 = np.sqrt(u_hist[0]**2 + v_hist[0]**2)

    c1 = axes[0].contourf(X, Y, speed0, levels=50, cmap="viridis")
    c2 = axes[1].contourf(X, Y, p_hist[0], levels=50, cmap="coolwarm")

    axes[0].set_title("Velocity magnitude")
    axes[1].set_title("Pressure")

    def update(frame):
        nonlocal c1, c2

        # Remove old contours (correct way)
        c1.remove()
        c2.remove()

        speed = np.sqrt(u_hist[frame]**2 + v_hist[frame]**2)

        c1 = axes[0].contourf(X, Y, speed, levels=50, cmap="viridis")
        c2 = axes[1].contourf(X, Y, p_hist[frame], levels=50, cmap="coolwarm")

        return []

    anim = FuncAnimation(fig, update, frames=len(u_hist), interval=interval)

    if save:
        anim.save(filename, dpi=200)

    plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_vectors(x, y, u_hist, v_hist,
                    stride=3, interval=50,
                    save=False, filename="vectors.mp4"):
    """
    Animate velocity vector (quiver) field.

    Parameters
    ----------
    x, y : 1D arrays
        Grid coordinates
    u_hist, v_hist : list of 2D arrays
        Velocity history
    stride : int
        Plot every stride-th vector
    interval : int
        Delay between frames (ms)
    save : bool
        Save animation to file
    filename : str
        Output filename
    """

    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(6, 6))

    # Initial quiver
    q = ax.quiver(
        X[::stride, ::stride],
        Y[::stride, ::stride],
        u_hist[0][::stride, ::stride],
        v_hist[0][::stride, ::stride]
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Velocity vectors")
    ax.set_aspect("equal")

    def update(frame):
        q.set_UVC(
            u_hist[frame][::stride, ::stride],
            v_hist[frame][::stride, ::stride]
        )
        ax.set_title(f"Velocity vectors (step {frame})")
        return q,

    anim = FuncAnimation(
        fig,
        update,
        frames=len(u_hist),
        interval=interval,
        blit=False
    )

    if save:
        anim.save(filename, dpi=200)

    plt.show()
