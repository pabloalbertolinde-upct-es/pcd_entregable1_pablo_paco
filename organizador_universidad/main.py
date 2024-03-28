from persona import Profesor, Alumno, Investigador
from organizacion import Asignatura, Departamento

class Universidad:

    def __init__(self,nombre_uni):
        self.nombre_uni = nombre_uni
        self.ualumnos=[]
        self.uprofesores=[]
        self.uasignaturas=[]
        self.udepartamentos=[]

    def add_alumno(self, dni, nombre, direccion, sexo):
        nuevo_alumno = Alumno(dni, nombre, direccion, sexo)
        self.ualumnos.append(nuevo_alumno)
        return nuevo_alumno

    def add_profesor(self, dni, nombre, direccion, sexo, dep):
        nuevo_profesor = Profesor(dni, nombre, direccion, sexo, dep)
        self.uprofesores.append(nuevo_profesor)
        return nuevo_profesor
    
    def add_asignatura(self, nombre, creditos=6):
        nueva_asignatura = Asignatura(nombre, creditos)
        self.uasignaturas.append(nueva_asignatura)
        return nueva_asignatura

    def add_departamento(self, nombre):
        nuevo_departamento = Departamento(nombre)
        self.udepartamentos.append(nuevo_departamento)
        return nuevo_departamento
    
    def asignar_persona_asignatura(self, persona, asignatura):
        persona.asignar_asignatura(asignatura)

    def desasignar_persona_asignatura(self, persona, asignatura):
        persona.desasignar_asignatura(asignatura)

#   def cambiar_profesor_dep(self, profesor, nuevo_dep):
#       profesor.dep.departamento_quitar(profesor)
#       nuevo_dep.departamento_añadir(profesor)
#       profesor.dep = nuevo_dep
        
    def cambiar_investigador_area(self, investigador, nueva_area):
        if isinstance(investigador, Investigador):
            investigador.cambio_area(self, nueva_area)
        else:
            print("El profesor no es titular")

    def borrar(self, persona):
        if isinstance(persona, Profesor):
            self.uprofesores.remove(persona)
            self.udepartamentos.remove(persona)     
        elif isinstance(persona, Alumno):
            self.ualumnos.remove(persona)
        persona.abandona_universidad()

    def mostrar_alumnos(self):
        print(f"Los alumnos de {self.nombre_uni} son: "+", ".join(str(alumno.nombre_per) for alumno in self.ualumnos))
    
    def mostrar_profesores(self):
        print(f"Los profesores de {self.nombre_uni} son: "+", ".join(str(profesor.nombre_per) for profesor in self.uprofesores))
    
    def mostrar_asignaturas(self):
        print(f"Las asignaturas de {self.nombre_uni} son: "+", ".join(str(asignatura.nombre_as) for asignatura in self.uasignaturas))
    
    def mostrar_departametos(self):
        print(f"Los departamentos de {self.nombre_uni} son: "+", ".join(str(dep.nombre_dep) for dep in self.udepartamentos))