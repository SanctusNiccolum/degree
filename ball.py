"""Count angle of deflection."""

from math import floor, pi


def degree(time: float, acc: float, rad: float, vel: float) -> int:
    """Count angle.

    Args:
        time (float): time
        acc (float): acceleration
        rad (float): radius
        vel (float): speed

    Returns:
        (int): result.
    """
    lenght = 2 * pi * rad
    way = vel * time + acc * time ** 2 / 2
    turn = way / lenght
    circle = 360
    return int(circle * (abs(floor(turn) - turn)))
