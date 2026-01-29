# Import standard library
import math

def volume_cylinder(radius: float, height: float) -> float:
    """
    Computes the volume of a right circular cylinder.

    Args:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder, computed as π * radius² * height.

    Examples:
        >>> volume_cylinder(3, 5)
        141.3716694115407
    """
    return math.pi * radius**2 * height


if __name__ == "__main__":
    radius, height = 2.0, 3.0
    volume = volume_cylinder(radius=radius, height=height)
    print(f"Volume of cylinder (radius={radius} m, height={height} m): {volume:0.3f} m³\n\n")
