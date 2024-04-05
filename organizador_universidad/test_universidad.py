from main import Universidad
from organizacion import Departamento, Asignatura
from persona import Persona, Profesor, Alumno, Investigador
import pytest as tst


def test_clases():
    """Esta funcion comprobara que la clase Universidad crea de manera correcta todas las instancias"""
    upct=Universidad("UPCT")
    dep1, dep2, dep3 = upct.add_departamentos()
    
    assert isinstance(dep1,Departamento) and  isinstance(dep2,Departamento) and isinstance(dep3, Departamento)

    profesor_prueba = upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1)
    Investigador_prueba = upct.add_profesor("dni", "titular", "calle", "Masculino", dep2, "area")

    assert isinstance(profesor_prueba, Profesor) and  isinstance(Investigador_prueba, Investigador)

    alumno_prueba = upct.add_alumno("dni", "alumno", "su calle", "Femenino")
    
    assert isinstance(alumno_prueba, Alumno)

    Asignatura_prueba = upct.add_asignatura("POO")
    
    assert isinstance (Asignatura_prueba, Asignatura)

def test_profesor_departamentos():
    """Comprobamos que el metodo add_profesor del departamento devuelve un error si se introducen dos departamentos"""
    # Creamos una instancia de Universidad
    upct = Universidad("UPCT")
    # Agregamos tres departamentos
    dep1, dep2, dep3 = upct.add_departamentos()

    # Intentamos agregar un profesor a dos departamentos diferentes
    with tst.raises(ValueError):
        upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1, dep2)

    prueba_cambio_area = upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1, "area de prueba")

    with tst.raises(ValueError):
        upct.cambiar_investigador_area(prueba_cambio_area, dep2)

