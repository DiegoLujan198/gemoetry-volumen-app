# Import standard libraries
import math


def volume_cone(base_radius: float, height: float) -> float:
    """
    Computes the volume of a right circular cone.

    Args:
        base_radius (float): The radius of the base of the cone.
        height (float): The height of the cone.

    Returns:
        float: The volume of the cone, calculated as (1/3) * π * base_radius^2 * height.

    Examples:
        >>> volume_cone(3.0, 5.0)
        47.12388980384689
    """
    return (1/3) * math.pi * base_radius**2 * height


if __name__ == "__main__":
    base_radius, height = 2.0, 6.5
    volume = volume_cone(base_radius=base_radius, height=height)
    print(f"Volume of cone (base_radius={base_radius} m, height={height} m): {volume:0.3f} m³\n\n")