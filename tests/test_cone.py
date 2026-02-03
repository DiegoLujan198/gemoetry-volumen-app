
import pytest
import math
from geometry.cone import volume_cone

def test_volume_cone_valid():
    # Siguiendo el ejemplo que tenemos en el cone.py
    assert volume_cone(3.0,5.0) == pytest.approx(47.12388, rel = 1e-6)

def test_volume_cone_negative():
    #Esta vez vamos a ver como se comporta si la radio de la base o la altura sea negativo
    # Radio = 2 y Altura = -5 
    # The volume of the cone, calculated as (1/3) * π * base_radius^2 * height.
    assert volume_cone(2.0, -5.0) == pytest.approx(-20.943951, rel = 1e-6)

def test_volume_cone_approx():
    #Prueba de flotantes generica
    r, h = 2.0, 6.5
    expected = (1/3)*math.pi* r**2 * h
    assert volume_cone(r,h) == pytest.approx(expected)