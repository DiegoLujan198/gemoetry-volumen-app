# Import standard library
import math


def volume_sphere(radius: float) -> float:
    """Compute the volume of a sphere.

    Args:
        radius (float): Radius of the sphere. Must be non-negative.

    Returns:
        float: Volume of the sphere.

    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative")

    return (4 / 3) * math.pi * radius ** 3

if __name__=='__main__':

    radius=2.0
    volume_sphere = volume_sphere(radius=radius)
    print(f"Volume of sphere (radius={radius} m): {volume_sphere:0.3f} m³\n")
