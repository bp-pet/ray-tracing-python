from src.vector import Vector

class SimpleImage:

    def __init__(self, pixels = list[list[Vector]]):
        """
        Create an image. Given data must be list of rows (lists), where each
        row is a list of pixels (tuples). Each pixel has 3 color values (RGB).

        Minimum size is 0, 0.

        Data is validated on object creation.
        """
        self.pixels = pixels
        self.validate()
        self.num_rows = len(pixels)
        self.num_cols = len(pixels[0])

    def validate(self) -> None:
        """Make sure given data is a valid image."""
        assert len(self.pixels) > 0
        num_cols = len(self.pixels[0])
        assert num_cols > 0
        for row in self.pixels:
            assert len(row) == num_cols

    def get_pmm(self) -> str:
        result = f"P3\n{self.num_rows} {self.num_cols}\n255\n"
        for row in self.pixels:
            for pixel in row:
                result += f"{int(pixel.x)} {int(pixel.y)} {int(pixel.z)}\n"
        return result


if __name__=="__main__":
    # test image generation
    pixels = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append((i, j, 0))
        pixels.append(row)
    
    img = SimpleImage(pixels)

    with open("output/test_output.pmm", "w") as f:
        f.write(img.get_pmm())