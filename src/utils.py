"""Module with utilities."""

import random


def get_random_point_on_unit_disk() -> tuple[float, float]:
    """Get a point on the unit disk with a uniform distribution."""
    while True:
        # generate a point in unit square, reject if not in unit disc
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1
        if x**2 + y**2 > 1:
            continue
        return x, y


if __name__ == "__main__":
    """Basic tests for the utils."""
    print(get_random_point_on_unit_disk())
