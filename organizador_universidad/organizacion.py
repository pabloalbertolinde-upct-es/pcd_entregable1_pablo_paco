from persona import Profesor, Alumno

class Asignatura:

    def __init__(self, nombre, creditos=6):
        self.nombre_as = nombre  
        self.creditos = creditos 
        self.profesores_as = [] 
        self.alumnos = []  

    def asignatura_añadir(self, persona):
        """Agrega un profesor o alumno a la asignatura."""
        if persona not in self.profesores_as and persona not in self.alumnos:
            if isinstance(persona, Alumno):
                self.alumnos.append(persona)
            elif isinstance(persona, Profesor):
                self.profesores_as.append(persona)

    def asignatura_quitar(self, persona):
        """Quita un profesor o alumno de la asignatura."""
        if isinstance(persona, Alumno) and persona in self.alumnos:
            self.alumnos.remove(persona)
        elif isinstance(persona, Profesor) and persona in self.profesores_as:
            self.profesores_as.remove(persona)
        
    def mostrar_profesoress(self):
        """Retorna una cadena con los profesores de esta asignatura."""
        a = 'Los profesores de esta asignatura son:'
        for p in self.profesores_as:
            a += '\n'
            a += p.nombre_per
        return a
    
    def mostrar_alumnos(self):
        """Retorna una cadena con los alumnos de esta asignatura."""
        a = 'Los alumnos matriculados son:'
        for p in self.alumnos:
            a += '\n'
            a += p.nombre_per
        return a
    
    def __str__(self):
        """Retorna una cadena representando la información de la asignatura."""
        salida = ''
        salida += 'Nombre: ' + self.nombre_as
        salida += ', Créditos: ' + str(self.creditos)
        salida += ', (Profesores: '
        salida += ', '.join([str(p.nombre_per) for p in self.profesores_as]) + ')'
        salida += ', (Alumnos: '
        salida += ', '.join([str(p.nombre_per) for p in self.alumnos]) + ')'
        return salida

#----------------------------------------------
    
class Departamento:

    def __init__(self, nombre):
        self.nombre_dep = nombre  # Nombre del departamento
        self.profesoress_dep = []  # Lista de profesores en el departamento
        
    def departamento_añadir(self, persona):
        """Agrega un profesor al departamento."""
        if persona in self.profesoress_dep:
            print("El profesor ya pertenecía al departamento")
        elif isinstance(persona, Profesor):
            self.profesoress_dep.append(persona)
        else:
            print('El objeto no es una instancia de profesor')
        
    def departamento_quitar(self, persona):
        """Quita un profesor del departamento."""
        if isinstance(persona, Profesor):
            if persona in self.profesoress_dep:
                self.profesoress_dep.remove(persona)
            else:
                print('Esa persona no se encuentra en este departamento')
        else:
            print('El objeto no es una instancia de profesor')
        
    def __str__(self):
        """Retorna una cadena representando la información del departamento."""
        salida = ''
        salida += 'Nombre: ' + self.nombre_dep
        salida += ', (Profesores: '
        salida += ', '.join([str(p.nombre_per) for p in self.profesoress_dep]) + ')'
        return salida
    
#--------------------------------------------------------