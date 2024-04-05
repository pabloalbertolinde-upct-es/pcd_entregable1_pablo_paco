from persona import Persona, Profesor, Alumno, Investigador
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

    def add_profesor(self, dni, nombre, direccion, sexo, dep, area = None):
        if area is None:    
            nuevo_profesor = Profesor(dni, nombre, direccion, sexo, dep)
            self.uprofesores.append(nuevo_profesor)
            return nuevo_profesor
        elif  isinstance(area, Departamento):
            raise ValueError("Un profesor no puede tener dos departamentos")
        else:
            nuevo_profesor = Investigador(dni, nombre, direccion, sexo, dep, area)
            self.uprofesores.append(nuevo_profesor)
            return nuevo_profesor
    
    def add_asignatura(self, nombre, creditos=6):
        nueva_asignatura = Asignatura(nombre, creditos)
        self.uasignaturas.append(nueva_asignatura)
        return nueva_asignatura

    def add_departamentos(self):
        """Solo se permiten estos departamentos: DIIC, DITEC, DIS. Ejemplo de uso: dep1, dep2, dep3 = upct.add_departamentos()"""
        DIIC = Departamento("DIIC")
        DITEC = Departamento("DITEC")
        DIS = Departamento("DIS")
        self.udepartamentos.append(DIIC)
        self.udepartamentos.append(DITEC)
        self.udepartamentos.append(DIS)
        return DIIC, DITEC, DIS
    
    def asignar_persona_asignatura(self, persona, asignatura):
        if isinstance(persona, Persona):
            persona.asignar_asignatura(asignatura)

    def desasignar_persona_asignatura(self, persona, asignatura):
        if isinstance(persona, Persona):
            persona.desasignar_asignatura(asignatura)

    def cambiar_profesor_dep(self, profesor, nuevo_dep):
        if isinstance(profesor, Profesor):
            if isinstance(nuevo_dep, Departamento):
                profesor.dep.departamento_quitar(profesor)
                nuevo_dep.departamento_añadir(profesor)
                profesor.dep = nuevo_dep
            else:
                print("El segundo parámetro debe ser un departamento")
        else:
            print("El primer parámetro debe ser un profesor")
        
    def cambiar_investigador_area(self, investigador, nueva_area):
        if isinstance(investigador, Investigador):
            if not isinstance(nueva_area, Departamento):
                investigador.cambio_area(nueva_area)
            else:
                raise ValueError("un profesor no puede tener dos departamentos")
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