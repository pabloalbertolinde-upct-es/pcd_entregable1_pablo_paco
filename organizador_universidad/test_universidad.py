from main import Universidad
from organizacion import Departamento, Asignatura
from persona import Profesor, Alumno, Investigador
import pytest as tst

def test_clases():
    """Esta funcion comprobara que la clase Universidad crea de manera correcta todas las instancias"""
    upct=Universidad("UPCT")
    dep1, dep2, dep3 = upct.add_departamentos()
    
    assert isinstance(dep1,Departamento) and  isinstance(dep2,Departamento) and isinstance(dep3, Departamento)

    profesor_prueba = upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1)
    Investigador_prueba = upct.add_profesor("dni", "titular", "calle", "Masculino", dep2, "area")

    assert isinstance(profesor_prueba, Profesor) and  isinstance(Investigador_prueba, Investigador)
    assert profesor_prueba in upct.uprofesores
    assert Investigador_prueba in upct.uprofesores

    alumno_prueba = upct.add_alumno("dni", "alumno", "su calle", "Femenino")
    
    assert isinstance(alumno_prueba, Alumno) and alumno_prueba in upct.ualumnos
    

    Asignatura_prueba = upct.add_asignatura("prueba")
    
    assert isinstance (Asignatura_prueba, Asignatura) and Asignatura_prueba in upct.uasignaturas

def test_asignar_desasignar():
    """comprobaremos que funcionen los metodos asignar y desasignar"""
    upct = Universidad("UPCT")
    upct = Universidad("UPCT")
    dep1, dep2, dep3 = upct.add_departamentos()
    profesor_prueba = upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1)
    Investigador_prueba = upct.add_profesor("dni", "titular", "calle", "Masculino", dep1, "area")
    alumno_prueba = upct.add_alumno("dni", "alumno", "su calle", "Femenino")
    Asignatura_prueba = upct.add_asignatura("prueba")

    upct.asignar_persona_asignatura(profesor_prueba, Asignatura_prueba)
    upct.asignar_persona_asignatura(alumno_prueba, Asignatura_prueba)
    upct.asignar_persona_asignatura(Investigador_prueba, Asignatura_prueba)
    
    #comprobamos el metodo asignar_persona_asignatura
    assert alumno_prueba in Asignatura_prueba.alumnos
    assert profesor_prueba in Asignatura_prueba.profesore_as
    assert Investigador_prueba in Asignatura_prueba.profesore_as

    upct.desasignar_persona_asignatura(profesor_prueba, Asignatura_prueba)
    upct.desasignar_persona_asignatura(alumno_prueba, Asignatura_prueba)
    upct.desasignar_persona_asignatura(Investigador_prueba, Asignatura_prueba)
    
    #comprobamos el metodo asignar_persona_asignatura
    assert alumno_prueba not in Asignatura_prueba.alumnos
    assert profesor_prueba not in Asignatura_prueba.profesore_as
    assert Investigador_prueba not in Asignatura_prueba.profesore_as

def test_profesor_departamentos():
    """Comprobamos que el metodo add_profesor del departamento devuelve un error si se introducen
    dos departamentos y que funciona el metodo cambiar_profesor_dep"""
    # Creamos una instancia de Universidad
    upct = Universidad("UPCT")
    # Agregamos tres departamentos
    dep1, dep2, dep3 = upct.add_departamentos()

    # Intentamos agregar un profesor a dos departamentos diferentes
    with tst.raises(ValueError):
        upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1, dep2)

    prof_cambio_dep = upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1, "area de prueba")

    with tst.raises(ValueError):
        upct.cambiar_investigador_area(prof_cambio_dep, dep2)
    upct.cambiar_profesor_dep(prof_cambio_dep,dep2)
    assert prof_cambio_dep.dep == dep2

def test_aprobar_asignatura():
    """comprueba el metodo aprobar_asignatura de alumno"""
    upct = Universidad("UPCT")
    alumno_prueba = upct.add_alumno("dni", "prueba", "calle prueba", "Masculino")
    asignatura_prueba = upct.add_asignatura("prueba")
    with tst.raises(TypeError):
        upct.alumno_aprueba_asignatura(alumno_prueba, asignatura_prueba)
    upct.asignar_persona_asignatura(alumno_prueba,asignatura_prueba)
    upct.alumno_aprueba_asignatura(alumno_prueba, asignatura_prueba)
    assert asignatura_prueba in alumno_prueba.asignaturas_aprobadas

def test_cambio_area():
    upct = Universidad("UPCT")
    dep1, dep2, dep3 = upct.add_departamentos()
    area="area"
    Investigador_prueba_area = upct.add_profesor("dni", "titular", "calle", "Masculino", dep2, area)
    nueva_area="nueva area"
    upct.cambiar_investigador_area(Investigador_prueba_area, nueva_area)
    assert Investigador_prueba_area.area == nueva_area

def test_borrar():
    """comprobamos el metodo borrar"""
    upct = Universidad("UPCT")
    dep1, dep2, dep3 = upct.add_departamentos()
    profesor_prueba = upct.add_profesor("dni", "profesor", "su calle", "Femenino", dep1)
    Investigador_prueba = upct.add_profesor("dni", "titular", "calle", "Masculino", dep1, "area")
    alumno_prueba = upct.add_alumno("dni", "alumno", "su calle", "Femenino")
    Asignatura_prueba = upct.add_asignatura("prueba")

    upct.asignar_persona_asignatura(profesor_prueba, Asignatura_prueba)
    upct.asignar_persona_asignatura(alumno_prueba, Asignatura_prueba)
    upct.asignar_persona_asignatura(Investigador_prueba, Asignatura_prueba)

    upct.borrar(profesor_prueba)
    upct.borrar(Investigador_prueba)
    upct.borrar(alumno_prueba)
    
    #vemos que no esten en la universidad
    assert profesor_prueba not in upct.uprofesores
    assert Investigador_prueba not in upct.uprofesores
    assert alumno_prueba not in upct.ualumnos
    
    #vemos que no esten en la asignatura a la que lo hemos asignado
    assert alumno_prueba not in Asignatura_prueba.alumnos
    assert profesor_prueba not in Asignatura_prueba.profesore_as
    assert Investigador_prueba not in Asignatura_prueba.profesore_as

    #vemos que los profesores no esten en el departamento en el que los hemos asignado
    assert profesor_prueba not in dep1.profesores_dep
    assert Investigador_prueba not in dep1.profesores_dep
    


    


