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

    Parametres
    ----------
    time : `npt.NDArray[np.float64]`
        The times to calculate the velocities at in seconds (s).
    gravity : `float`, optional
        The gravity in metres per second squared (m/s^2), by default 9.80665
    drag_coefficient : `float`, optional
        The linear drag coefficient of the object
        in newton-seconds per metre (N s/m),
        by default 0.0
    mass : `float`, optional
        The mass of the falling object in kilograms, by default 1.0
    initial_velocity : `float`
        The initial velocity of the falling object in metres per second (m/s),
        by default 0.0

    Returns
    -------
    `npt.NDArray`
        An array containing the velocities at each time in metres per second (m/s).
    """
    terminal_velocity = - mass / drag_coefficient * gravity

    return (
        terminal_velocity
        + (initial_velocity - terminal_velocity)
        * np.exp(- drag_coefficient / mass * time)
    )


def position(
    time: npt.NDArray[np.float64],
    gravity: float = 9.80665,
    drag_coefficient: float = 0,
    mass: float = 1.0,
    initial_velocity: float = 0,
    initial_position: float = 0
) -> npt.NDArray:
    """Return the position of a falling object at the given times.

    Parametres
    ----------
    time : `npt.NDArray[np.float64]`
        The times to calculate the velocities at in seconds (s).
    gravity : `float`, optional
        The gravity in metres per second squared (m/s^2), by default 9.80665
    drag_coefficient : `float`, optional
        The linear drag coefficient of the object
        in newton-seconds per metre (N s/m),
        by default 0.0
    mass : `float`, optional
        The mass of the falling object in kilograms, by default 1.0
    initial_velocity : `float`
        The initial velocity of the falling object in metres per second (m/s),
        by default 0.0
    initial_position : `float`
        The initial position of the falling object in metres (m),
        by default 0.0

    Returns
    -------
    `npt.NDArray`
        An array containing the velocities at each time in metres per second (m/s).
    """
    terminal_velocity = - mass / drag_coefficient * gravity

    return (
        initial_position
        + terminal_velocity * time
        + (terminal_velocity - initial_velocity) * (mass / drag_coefficient) *
        np.exp(- drag_coefficient / mass * time)
    )


if __name__ == "__main__":
    time_domain = np.linspace(0, 8)

    plt.title("Velocity vs Time")
    plt.ylabel("Velocity (m/s)")
    plt.xlabel("Time (s)")
    plt.plot(time_domain, velocity(time_domain, drag_coefficient=1.0))
    plt.savefig(Path("vol1-mechanics/assets/drag-velocity.pgf"))
    plt.show()

    plt.title("Position vs Time")
    plt.ylabel("Position (m)")
    plt.xlabel("Time (s)")
    plt.plot(time_domain, position(time_domain, drag_coefficient=1.0))
    plt.savefig(Path("vol1-mechanics/assets/drag-position.pgf"))
    plt.show()
