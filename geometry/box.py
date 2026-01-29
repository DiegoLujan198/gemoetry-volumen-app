def volume_box(width: float, height: float, depth: float) -> float:
    """
    Computes the volume of a rectangular box.

    Args:
        width (float): The width of the box.
        height (float): The height of the box.
        depth (float): The depth of the box.

    Returns:
        float: The volume of the box, calculated as width * height * depth.

    Examples:
        >>> volume_box(2.0, 3.0, 4.0)
        24.0
    """
    return width * height * depth


if __name__ == "__main__":
    width, height, depth = 2.0, 3.0, 4.0
    volume = volume_box(width=width, height=height, depth=depth)
    print(f"Volume of box (width={width} m, height={height} m, depth={depth} m): {volume:0.3f} m³\n\n")