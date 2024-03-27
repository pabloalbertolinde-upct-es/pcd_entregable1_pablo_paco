#from organizacion import Asignatura, Departamento

class Persona:
    def __init__(self, dni, nombre, direccion, sexo):
        self.dni = dni
        self.nombre_per = nombre
        self.direccion = direccion
        self.sexo = sexo
        self.asignaturas_asignadas=[]
    
    
    
    def abandona_universidad(self):
        """
        Desasigna a la persona de todas sus asignaturas.
        En Python, no hay una forma directa de eliminar una instancia desde dentro de sus propios métodos.
        Si se desea eliminar la instacia por completo,
        DEBE DE EJECUTARSE ESTE MÉTODO PREVIAMENTE y después, del persona,
        siendo persona la instancia a eliminar.
        """
        for asignatura in self.asignaturas_asignadas:
            self.desasignar_asignatura(asignatura)
        if isinstance(self, Profesor):
            print("ha llegado")
            self.dep.departamento_quitar(self)



    def asignar_asignatura(self, asignatura):
        #if self.no_asignada(asignatura):
        if asignatura not in self.asignaturas_asignadas:
            self.asignaturas_asignadas.append(asignatura)
            asignatura.asignatura_añadir(self)
        else:
            pass
        #else:
        #    raise ValueError("La persona ya tiene asignada la asignatura")
    
    
    
    def desasignar_asignatura(self, asignatura):
        if asignatura in self.asignaturas_asignadas:
            self.asignaturas_asignadas.remove(asignatura)
            asignatura.asignatura_quitar(self)
        else:
            print(self.nombre_per, " no tenia esa asignatura.")
            pass
            #raise ValueError("La persona no tiene asignada la asignatura")
#    def nombre_persona(self):
#        return self.nombre
    
    
    
    def mostrar_asignaturas(self):
        return f"las asignaturas de {self.nombre_per} son: "+", ".join(str(asignatura.nombre_as) for asignatura in self.asignaturas_asignadas)
   
   
   
    def __str__(self):
        a = ''
        a += 'Nombre: '+ self.nombre_per
        a += ", DNI: " + self.dni
        a += ", Dirección: " + self.direccion
        a += ", Asignaturas asignadas: " + self.mostrar_asignaturas()
        if isinstance(self, Profesor):
            a += ", Departamento: " + self.dep.nombre_dep
        if isinstance(self, Investigador):
            a += ", Area de investigación: " + self.area
        return a
#-----------------------------------------------

#-----------------------------------------------
    


class Alumno(Persona):
    def __init__(self, dni, nombre, direccion, sexo):
        Persona.__init__(self, dni, nombre, direccion, sexo)



#-----------------------------------------------
class Profesor(Persona): #asociados          #HAY QUE HACER QUE SOLO PUEDAN PERTENECER A UN DEPARTAMENTO Y QUE EL DEP SEA UNO DE LOS DEL ENUNCIADO
    def __init__(self, dni, nombre, direccion, sexo, dep):
#       if dep not in Departamento.departamentos:
#           raise ValueError("El departamento no existe. Departamentos existentes: DIIC, DITEC, DIS")
#       else:
            Persona.__init__(self, dni, nombre, direccion, sexo)
            self.dep = dep
            dep.departamento_añadir(self)



    def cambio_dep(self, dep):
        if isinstance(dep, Departamento):
            self.dep = dep
        else:
            raise ValueError("El departamento no existe. \nDepartamentos existentes: DIIC, DITEC, DIS")
        


class Investigador(Profesor): #titulares
    def __init__(self, dni, nombre, direccion, sexo, dep, area):
        Profesor.__init__(self, dni, nombre, direccion, sexo, dep)
        self.area = area
    def cambio_area(self, area):
        self.area = area
#--------------------------------------------------------------------------------------------