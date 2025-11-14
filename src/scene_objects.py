"""All types of objects that can be added to a scene."""

import math

from src.vector import Vector, dot


class SceneObject:
    """Abstract class for scene objects."""

    def __init__(self, color: Vector, roughness: float):
        self.color = color
        self.roughness = roughness

    def intersect_ray(
        self, p: Vector, v: Vector, t_min: float, t_max: float
    ) -> float | None:
        """Find the smallest value of t in a given interval, where a ray p + t * v
        intersects the object."""
        pass

    def get_unit_normal_at_point(self, p: Vector) -> Vector:
        """Get the unit normal of a point with respect to the object."""
        return Vector(0, 0, 0)


class Sphere(SceneObject):
    """Sphere represented by a center position and a radius."""

    def __init__(self, center: Vector, radius: float, color: Vector, roughness: float):
        """Create a sphere."""
        self.center = center
        self.radius = radius
        self.color = color
        assert 0 <= roughness <= 1, "Roughness must be between 0 and 1"
        self.roughness = roughness

    def __str__(self):
        return f"Sphere with center {self.center}, radius {self.radius}, color {self.color}"

    def intersect_ray(
        self, p: Vector, v: Vector, t_min: float, t_max: float
    ) -> float | None:
        """Given a ray with origin p and direction v, find the
        distance to the intersection, or return None if there isn't one.

        Returns the smaller t value that is in the given interval.

        Derivation:

        Let (x0, y0, z0) be the center of the sphere and r the radius.

        (p.x + t * v.x - x0) ** 2
        + (p.y + t * v.y - y0) ** 2
        + (p.z + t * v.z - z0) ** 2
        = r ** 2

        (vx ** 2 + vy ** 2 + vz ** 2) * t ** 2
        + 2 * ((px - x0) * vx + (py - y0) * vy + (pz - z0) * vz) * t
        + (px - x0) ** 2  + (py - y0) ** 2 + (pz - z0) ** 2 - r ** 2

        Use abc formula. Rewrite as vector operations.
        """

        a = v.squared_magnitude()
        b = 2 * dot(p - self.center, v)
        c = (p - self.center).squared_magnitude() - self.radius**2

        assert a != 0, "Ray with 0 direction given"

        D = b**2 - 4 * a * c

        if D < 0:
            # no intersection.
            return None

        sqrtD = math.sqrt(D)

        t1 = (-b + sqrtD) / (2 * a)
        t2 = (-b - sqrtD) / (2 * a)

        # check if results are in interval
        t1_checked = t1 if t_min <= t1 <= t_max else None
        t2_checked = t2 if t_min <= t2 <= t_max else None

        # return smaller result
        if t1_checked is None and t2_checked is None:
            return None
        if t1_checked is None:
            return t2_checked
        if t2_checked is None:
            return t1_checked
        return min(t1_checked, t2_checked)

    def get_unit_normal_at_point(self, p: Vector) -> Vector:
        """
        Calculate the normal at a point. If the point is not on
        the sphere, it will be effectively projected on it.
        """
        return (p - self.center).unit()
