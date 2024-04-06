class Persona:

    def __init__(self, dni, nombre, direccion, sexo):
        self.dni = dni
        self.nombre_per = nombre
        self.direccion = direccion
        self.sexo = sexo
        self.asignaturas_asignadas=[]
    
    def abandona_universidad(self):
        """
        Desasigna a la persona de todas sus asignaturas y departamento si es profesor.
        """
        
        for asignatura in self.asignaturas_asignadas:
            print(asignatura.nombre_as)
            self.desasignar_asignatura(asignatura)
        if isinstance(self, Profesor):
            
            self.dep.departamento_quitar(self)

    def asignar_asignatura(self, asignatura):
        """asigna una asignatura"""
        if asignatura not in self.asignaturas_asignadas:
            self.asignaturas_asignadas.append(asignatura)
            asignatura.asignatura_añadir(self)
        else:
            print(self.nombre_per, "ya tenia esa asignatura.")
    
    def desasignar_asignatura(self, asignatura):
        """desasigna la asignatura"""
        if asignatura in self.asignaturas_asignadas:
            self.asignaturas_asignadas.remove(asignatura)
            asignatura.asignatura_quitar(self)
        else:
            print(self.nombre_per, "no tenia esa asignatura.")
    
    def mostrar_asignaturas_persona(self):
        """Si quieres ver las asignaturas de una persona, use este método dentro de un print."""
        return f"las asignaturas de {self.nombre_per} son: "+", ".join(str(asignatura.nombre_as) for asignatura in self.asignaturas_asignadas)

    def __str__(self):
        """Se habilita el print de la instancia"""
        a = ''
        a += 'Nombre: '+ self.nombre_per
        a += ", DNI: " + self.dni
        a += ", Dirección: " + self.direccion
        a += ", Asignaturas asignadas: " + self.mostrar_asignaturas_persona()
        if isinstance(self, Profesor):
            a += ", Departamento: " + self.dep.nombre_dep
        if isinstance(self, Investigador):
            a += ", Area de investigación: " + self.area
        return a
    
#-----------------------------------------------

class Alumno(Persona):
    def __init__(self, dni, nombre, direccion, sexo):
        Persona.__init__(self, dni, nombre, direccion, sexo)
        self.asignaturas_aprobadas =  [] 
        
    def aprobar_asignatura(self, asignatura):
        """Añade una asignatura en la lista de asignaturas aprobadas"""
        if  asignatura in self.asignaturas_asignadas:
            self.desasignar_asignatura(asignatura) # Quitamos la asignatura del alumno
            self.asignaturas_aprobadas.append(asignatura)   # Y añadimos a las aprobadas
        else:
            raise TypeError("El alumno no estaba cursando esa asignatura")
        
#-----------------------------------------------
        
class Profesor(Persona): 

    def __init__(self, dni, nombre, direccion, sexo, dep):
        Persona.__init__(self, dni, nombre, direccion, sexo)
        self.dep = dep
        dep.departamento_añadir(self)

    
        
class Investigador(Profesor): 

    def __init__(self, dni, nombre, direccion, sexo, dep, area):
        Profesor.__init__(self, dni, nombre, direccion, sexo, dep)
        self.area = area

    def cambio_area(self, area):
        """cambia el area del investigador"""
        self.area = area

#--------------------------------------------------------------------------------------------