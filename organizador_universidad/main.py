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
        """Añade un alumno"""
        nuevo_alumno = Alumno(dni, nombre, direccion, sexo)
        self.ualumnos.append(nuevo_alumno)
        return nuevo_alumno

    def add_profesor(self, dni, nombre, direccion, sexo, dep, area = None):
        """Añade un profesor"""
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
        """Añade una asignatura"""
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
        """asigna alumnos a una asignatura"""

        if isinstance(persona, Persona) and (persona in self.ualumnos or persona in self.uprofesores):
            persona.asignar_asignatura(asignatura)

    def desasignar_persona_asignatura(self, persona, asignatura):
        """desasigna alumnos a una asignatura"""
        if isinstance(persona, Persona):
            persona.desasignar_asignatura(asignatura)

    def cambiar_profesor_dep(self, profesor, nuevo_dep):
        """cambia un profesor de departamento"""
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
        """cambia un investigador de area"""
        if isinstance(investigador, Investigador):
            if not isinstance(nueva_area, Departamento):
                investigador.cambio_area(nueva_area)
            else:
                raise ValueError("un profesor no puede tener dos departamentos")
        else:
            print("El profesor no es titular")

    def borrar(self, persona):
        "borra una persona del sistema"
        if isinstance(persona, Profesor):
            print("Eliminando profesor...")
            self.uprofesores.remove(persona)           
            persona.abandona_universidad()
            
            
        elif isinstance(persona, Alumno):
            print("alumno abandona universidad")
            persona.abandona_universidad()
            self.ualumnos.remove(persona)
            
        if  isinstance(persona, Persona):
            del persona
            
    

    #-------------------------------Los siguientes metodos muestran un tipo de instancia especifica
    def mostrar_alumnos(self):
        print(f"Los alumnos de {self.nombre_uni} son: "+", ".join(str(alumno.nombre_per) for alumno in self.ualumnos))
    
    def mostrar_profesores(self):
        print(f"Los profesores de {self.nombre_uni} son: "+", ".join(str(profesor.nombre_per) for profesor in self.uprofesores))
    
    def mostrar_asignaturas(self):
        print(f"Las asignaturas de {self.nombre_uni} son: "+", ".join(str(asignatura.nombre_as) for asignatura in self.uasignaturas))
    
    def mostrar_departametos(self):
        print(f"Los departamentos de {self.nombre_uni} son: "+", ".join(str(dep.nombre_dep) for dep in self.udepartamentos))

    #Se ha decidido que print de universidad sea un resumen del sistema por la claridad del usuario

    def __str__(self):
        """permite hacer un print de la instancia"""
        informacion="Resumen de " + self.nombre_uni +"\n\n"

        departamentos =  "Departamentos:\n\n" 

        indep=""
        for departamento in self.udepartamentos:
            indep += departamento.nombre_dep + ":\nLos profesores del departamento son:\n\n"
            for profesor in departamento.profesores_dep:
                indep += profesor.nombre_per + "\n"
            indep += "--------------------\n\n"
            
        informacion += departamentos + indep + "Asignaturas:\n\n"
        asig= ""
        
        for asignatura in self.uasignaturas:
            asig+= asignatura.nombre_as + ":\nEL/Los profesores de la asignatura son:\n\n"
            for profesor in asignatura.profesore_as:
                asig += profesor.nombre_per + "\n"

            asig+="\nLos alumnos de la asignatura son:\n\n"

            for alumno in asignatura.alumnos:
                asig += alumno.nombre_per + "\n"
            asig+="\n"
        informacion += asig+ "\n----------------------\n\nProfesores: \n\n"

        per = ""
        for profesor in self.uprofesores:
            per += profesor.nombre_per + "\n"

        per +="\n------------\n\nAlumnos:\n\n"

        for alumno in self.ualumnos:
            per += alumno.nombre_per + "\n"

        informacion += per
            

        return informacion
    
        

    
        