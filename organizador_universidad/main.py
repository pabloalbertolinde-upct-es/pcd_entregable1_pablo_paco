## CAMBIOS
# cambio de nombre de las listas de asignatura y departamento de self.profesores
# a self.profesores_as y self.profesores_dep
#
#   Eliminacion del metodo no_asignada y consecuente modificacion de asignatura_añadir, asignar_asignatura
#   y desasignar_asignatura
#   eliminacion del metodo nombre_persona y nombre_dep
#   cambio de los nombres de las variables nombre de cada clase
#
# Modificacion de departamento_quitar
from persona import Profesor, Alumno, Investigador
from organizacion import Asignatura, Departamento


class UPCT:



    def __init__(self):

        self.ualumnos=[]
        self.uprofesores=[]
        self.udepartamentos=[]
        self.uasignaturas=[]



    def add_profesor(self, dni, nombre, direccion, sexo, dep):
        nuevo_profesor = Profesor(dni, nombre, direccion, sexo, dep)
        self.uprofesores.append(nuevo_profesor)
        return self.uprofesores[-1]
        
        

    def add_alumno(self, dni, nombre, direccion, sexo):
        nuevo_alumno = Alumno(dni, nombre, direccion, sexo)
        self.ualumnos.append(nuevo_alumno)
        return self.ualumnos[-1]

    def asignar_profesor_asignatura():
        pass

    def cambiar_profesor_dep():
        pass

    def añadir_alumno_asignatura():
        pass

    def asignar_profesor_asignatura():
        pass


    def add_asignatura(self, nombre, creditos=6):
        nueva_asignatura = Asignatura(nombre, creditos)
        self.uasignaturas.append(nueva_asignatura)
        return self.uasignaturas[-1]



    def add_departamento(self, nombre):
        nuevo_departamento = Departamento(nombre)
        self.udepartamentos.append(nuevo_departamento)
        return self.udepartamentos[-1]



    def borrar(self, persona):
        if isinstance(persona, Profesor):
            # Busca el profesor en la lista de profesores y lo elimina
            
            self.uprofesores.remove(persona)
            self.udepartamentos.remove(persona)
            # Elimina al profesor del departamento que tenía asignado
            
        elif isinstance(persona, Alumno):
            self.ualumnos.remove(persona)

        persona.abandona_universidad()
        del persona





