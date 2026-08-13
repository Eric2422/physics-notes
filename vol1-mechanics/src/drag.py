import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

GRAVITY = 9.80665
DRAG_COEFFICIENT = 1
MASS = 1

terminal_velocity = MASS / DRAG_COEFFICIENT * GRAVITY


def velocity(initial_velocity: float, time: npt.NDArray[np.float64]) -> npt.NDArray:
    return terminal_velocity + \
        (terminal_velocity - initial_velocity) * \
        np.exp(- DRAG_COEFFICIENT / MASS * time)


if __name__ == "__main__":
    time_domain = np.linspace(0, 10)

    plt.plot(time_domain, velocity(0, time_domain))
    plt.show()
