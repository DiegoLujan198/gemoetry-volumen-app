import pytest
import math
from geometry.cylinder import volume_cylinder

def test_volume_cylinder_valid():
    # Siguiendo el ejemplo que tenemos en el cylinder.py
    assert volume_cylinder(3.0,5.0) == pytest.approx(141.3716694115407, rel = 1e-6)

def test_volume_cylinder_negative():
    #Esta vez vamos a ver como se comporta si el radio o la altura sea negativo
    #The volume of the cylinder, computed as π * radius² * height.
    # Radio = 2 y Altura = -3 
    assert volume_cylinder(2.0, -3.0) == pytest.approx(-37.6991, rel = 1e-6)

def test_volume_cylinder_approx():
    #Prueba de flotantes generica
    r, h = 1.5, 2.5
    expected = math.pi* r**2 * h
    assert volume_cylinder(r,h) == pytest.approx(expected)