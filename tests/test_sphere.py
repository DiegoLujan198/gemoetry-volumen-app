import pytest
import math
from geometry.sphere import volume_sphere

def test_volume_sphere_valid():
    # Usando un ejemplo si el sphere tendira un radio de 2
    assert volume_sphere(2.0) == pytest.approx(33.510321, rel = 1e-6)

def test_volume_sphere_negative():
    #A comparacion de los demas el sphere no puede tener un radio negativo, por ende tenemos que poner un error que indique que no es un valor valido
    #Para comprobar que este test se pueda saber si funciona como deberia, tenemos que poner volume_sphere que sea igual a un numero negativo
    #En este caso es igual a -1.0
    with pytest.raises(ValueError, match="Radius must be non-negative"):
        volume_sphere(-1.0)

def test_volume_sphere_approx():
    #Prueba de flotantes generica
    r = 1.0
    expected = (4/3)*math.pi* r**3 
    assert volume_sphere(r) == pytest.approx(expected)