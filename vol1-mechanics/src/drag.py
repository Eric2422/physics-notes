from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def velocity(
    time: npt.NDArray[np.float64],
    gravity: float = 9.80665,
    drag_coefficient: float = 0,
    mass: float = 1.0,
    initial_velocity: float = 0
) -> npt.NDArray:
    """Return the velocity of a falling object at the given times.

    Parameters
    ----------
    initial_velocity : `float`
        The initial velocity of the falling object in meters per second (m/s).
    time : `npt.NDArray[np.float64]`
        The times to calculate the velocities at in seconds (s).

    Returns
    -------
    `npt.NDArray`
        An array containing the velocities at each time in metres per second (m/s).
    """
    terminal_velocity = - mass / drag_coefficient * gravity

    return terminal_velocity + \
        (initial_velocity - terminal_velocity) * \
        np.exp(- drag_coefficient / mass * time)


if __name__ == "__main__":
    time_domain = np.linspace(0, 10)

    plt.title("Velocity vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.plot(time_domain, velocity(time_domain, drag_coefficient=1.0))
    plt.savefig(Path("../assets/drag-velocity.pgf"))
    plt.show()
