class Persona:

    def __init__(self, dni, nombre, direccion, sexo):
        self.dni = dni
        self.nombre_per = nombre
        self.direccion = direccion
        self.sexo = sexo
        self.asignaturas_asignadas = []  
    
    def abandona_universidad(self):
        """Desasigna a la persona de todas sus asignaturas y departamento si es profesor."""
        for asignatura in self.asignaturas_asignadas:
            self.desasignar_asignatura(asignatura)
        if isinstance(self, Profesor):
            self.dep.departamento_quitar(self)

    def asignar_asignatura(self, asignatura):
        """Asigna una asignatura a la persona."""
        if asignatura not in self.asignaturas_asignadas:
            self.asignaturas_asignadas.append(asignatura)
            asignatura.asignatura_añadir(self)
        else:
            print(self.nombre_per, "ya tenía esa asignatura.")
    
    def desasignar_asignatura(self, asignatura):
        """Desasigna una asignatura de la persona."""
        if asignatura in self.asignaturas_asignadas:
            self.asignaturas_asignadas.remove(asignatura)
            asignatura.asignatura_quitar(self)
        else:
            print(self.nombre_per, "no tenía esa asignatura.")
    
    def mostrar_asignaturas_persona(self):
        """Retorna una cadena con las asignaturas asignadas a la persona."""
        return f"Las asignaturas de {self.nombre_per} son: " + ", ".join(str(asignatura.nombre_as) for asignatura in self.asignaturas_asignadas)

    def __str__(self):
        """Retorna una cadena representando la información de la persona."""
        info_persona = ''
        info_persona += 'Nombre: ' + self.nombre_per
        info_persona += ", DNI: " + self.dni
        info_persona += ", Dirección: " + self.direccion
        info_persona += ", Asignaturas asignadas: " + self.mostrar_asignaturas_persona()
        if isinstance(self, Profesor):
            info_persona += ", Departamento: " + self.dep.nombre_dep
        if isinstance(self, Investigador):
            info_persona += ", Área de investigación: " + self.area
        return info_persona

#-----------------------------------------------

class Alumno(Persona):
    def __init__(self, dni, nombre, direccion, sexo):
        """Inicializa una instancia de Alumno utilizando los datos de Persona."""
        Persona.__init__(self, dni, nombre, direccion, sexo)

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
        """Cambia el área de investigación de un investigador."""
        self.area = area