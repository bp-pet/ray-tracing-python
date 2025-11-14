"""Light source related tools."""

from src.vector import Vector


class LightSource:
    """Light source represented just by a position."""

    def __init__(self, position: Vector) -> None:
        """Create a light source at a position."""
        self.position = position
        # TODO implement light color
