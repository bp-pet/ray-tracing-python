from src.camera import Camera
from src.light_source import LightSource
from src.scene import Scene
from src.scene_objects import SceneObject, Sphere
from src.vector import Vector


if __name__ == "__main__":
    """Specify objects and capture scene."""

    # camera distance 5 along the x-axis, pointed towards the origin
    camera = Camera(
        eye_position=Vector(5, 0, 1),
        window_size_x=1,
        window_size_y=1,
        viewing_direction=Vector(-1, 0, -0.1),
        orientation_vector=Vector(-0.1, 0, 1),
        window_distance=1,
    )

    scene_objects: list[SceneObject] = [
        Sphere(
            center=Vector(0, 2, 0),
            radius=1,
            color=Vector(240, 50, 31),
            roughness=1,
        ),
        Sphere(
            center=Vector(0, 0, 0), radius=1, color=Vector(31, 240, 33), roughness=0
        ),
        Sphere(
            center=Vector(0, -2, 0), radius=1, color=Vector(45, 31, 240), roughness=1
        ),
        Sphere(
            center=Vector(0, -4, 0),
            radius=1,
            color=Vector(240, 31, 219),
            roughness=0.2,
        ),
        Sphere(
            center=Vector(0, 4, 0),
            radius=1,
            color=Vector(240, 31, 219),
            roughness=0.8,
        ),
        Sphere(
            center=Vector(0, 0, -10000),
            radius=9999,
            color=Vector(129, 72, 176),
            roughness=1,
        ),
    ]

    light_sources = [
        LightSource(position=Vector(5, -2, 4)),
        LightSource(position=Vector(5, 1, 4)),
    ]  # currently not used

    scene = Scene(
        camera=camera, scene_objects=scene_objects, light_sources=light_sources
    )

    pmm = scene.capture(1000, 1000, verbose=True).get_pmm()

    with open("output/output.pmm", "w") as f:
        f.write(pmm)
