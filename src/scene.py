import numpy as np

from src.camera import Camera
from src.constants import background_color
from src.scene_objects import SceneObject
from src.light_source import LightSource
from src.simple_image import SimpleImage
from src.vector import Vector, dot


class Scene:
    def __init__(
        self,
        camera: Camera,
        scene_objects: list[SceneObject],
        light_sources: list[LightSource],
    ):
        self.camera = camera
        self.scene_objects = scene_objects
        self.light_sources = light_sources

    def capture(
        self, resolution_x: int, resolution_y: int, verbose: bool = False
    ) -> SimpleImage:
        """
        Capture the scene with a given resolution.

        x is top to bottom, y is left to right.

        Camera ray given by p + t * v or P + t * V in matrix form.
        """
        assert resolution_x > 0
        assert resolution_y > 0

        if not self.scene_objects:
            return np.tile(background_color, (1, resolution_x, resolution_y))

        pixels = []
        pixel_size_x = self.camera.window_size_x / resolution_x
        pixel_size_y = self.camera.window_size_y / resolution_y

        pixel_centers = np.zeros(3, pixel_size_x, pixel_size_y)  # 3 by x by y
        top_left = np.array(self.camera.top_left.get_tuple())  # 3
        up_unit = np.array(self.camera.up_unit.get_tuple())  # 3
        right_unit = np.array(self.camera.right_unit.get_tuple())  # 3
        # TODO write without loops
        for i in range(resolution_x):
            row = []
            for j in range(resolution_y):
                pixel_centers[:, i, j] = (
                    top_left
                    - ((i + 0.5) * 2 * pixel_size_x * up_unit)
                    + ((j + 0.5) * 2 * pixel_size_y * right_unit)
                )

        P = pixel_centers.reshape(3, -1)  # 3 by x*y
        V = P - self.camera.eye_position[:, np.newaxis]  # 3 by x*y

        distances = np.zeros(
            shape=(len(self.scene_objects), resolution_x, resolution_y)
        )  # n by x by y
        for obj_index, scene_object in enumerate(self.scene_objects):
            temp = scene_object.intersect_rays(
                self.camera.eye_position, V, 1, np.inf
            )  # n
            distances[obj_index, :, :] = temp.reshape(resolution_x, resolution_y)

        # UP TO HERE HAS BEEN REWRITTEN TO NUMPY

        collision_objects = argmin()

        collided_object = self.scene_objects[min_index]
        collision_point = self.camera.eye_position + min_distance * ray_direction
        unit_normal = collided_object.get_unit_normal_at_point(collision_point)

        total_illumination = 0.0
        for light_source in self.light_sources:
            ray_to_light_source = light_source.position - collision_point

            # check for shadow
            in_shadow = False
            for scene_object in self.scene_objects:
                if scene_object == collided_object:
                    continue
                shadow_distance = scene_object.intersect_ray(
                    collision_point, ray_to_light_source, 0, 1
                )
                if shadow_distance is not None:
                    in_shadow = True
                    break

            total_illumination += (
                max(0, dot(unit_normal, ray_to_light_source.unit()))
                if not in_shadow
                else 0
            )
        illumination = total_illumination / len(self.light_sources)
        # not sure this is a good way to do illumination but it doesn't matter for one source

        return SimpleImage(pixels)
