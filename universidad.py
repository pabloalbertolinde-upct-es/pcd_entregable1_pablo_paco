class Persona:
        def __init__(self, dni, nombre, direccion, sexo):
            self.dni = dni
            self.nombre = nombre
            self.direccion = direccion
            self.sexo = sexo

        def asesinar(self):

            # hay que quitar a todos los alumnos y profesores de todas las asignaturas,
            # ademas de borrar toda su informacion

            pass

        def asignar(self, asignatura):

            try:
                asignatura.asignar_profesor(self)

            except:
                asignatura.matricular_alumno(self)

        def quit(self, asignatura):
            try:
                asignatura.quitar_profesor(self)

            except:
                asignatura.quitar_alumno(self)

#-----------------------------------------------


class Alumno(Persona):
    def __innit__(self, dni, nombre, direccion, sexo):
        Profesor.__init__(self, dni, nombre, direccion, sexo)




#-----------------------------------------------

class titular(Persona):

    def __init__(self, dni, nombre, direccion, sexo, area):
        Profesor.__init__(self, dni, nombre, direccion, sexo)
        self.area = area

class Profesor(Persona):
    def __init__(self, dni, nombre, direccion, sexo):
        Persona.__init__(self, dni, nombre, direccion, sexo)

    def asignar_materia(self, materia):
        print("Asignando la materia {} al profesor con DNI {}".format(materia, self.dni))


#--------------------------------------------------------------------------------------------

class Asignatura:
    def __init__(self, nombre, creditos=6):
        '''iniciamos la clase Asignatura'''
        self.nombre = nombre  # Nombre de la asignatura
        self.creditos = creditos     # Número de créditos
        self.profesores = []   # Lista de profesores que imparten la asignatura
        self.alumnos = [] #lista de alumnos

    def añadir(self, persona):
        """Agrega un profesor o alumno a la asignatura"""
        if isinstance(persona, Alumno):
            self.alumnos.append(persona)

        elif isinstance(persona, Profesor):
            self.profesores.append(persona)

        else:
            raise TypeError('El objeto no es una instancia de la clase Alumno ni profesor')

    def agregar_profesor(self, profesor):
        """Agrega un profesor a la lista de profesores"""
        if isinstance(profesor, Profesor):
            self.profesores.append(profesor)
        else:
            raise TypeError('El objeto no es una instancia de la clase Profesor')

    def matricular_alumno(self, alumno):
        """Agrega un profesor a la lista de profesores"""
        if isinstance(alumno, Alumno):
            self.alumnos.append(alumno)
        else:
            raise TypeError('El objeto no es una instancia de la clase Alumno')

    def quitar(self, persona):
        """Agrega un profesor o alumno a la asignatura"""
        if isinstance(persona, Alumno) and persona in self.alumnos:
            self.alumnos.remove(persona)

        elif isinstance(persona, Profesor) and persona in self.profesores:
            self.profesores.remove(persona)

        else:
            raise TypeError('El objeto no es una instancia de la clase Alumno ni profesor')

    def quitar_profesor(self, profesor):
        """Quita un profesor de la lista de profesores"""

        self.profesores.remove(profesor)

    def quitar_alumno(self, alumno):
        """Quita un profesor de la lista de profesores"""

        self.profesores.remove(alumno)

    def añadir(self, persona):
        """Agrega un profesor a la lista de profesores"""
        if isinstance(persona, Alumno):
            self.alumnos.append(persona)

        elif isinstance(persona, Profesor):
            self.profesores.append(persona)

        else:
            raise TypeError('El objeto no es una instancia de la clase Alumno ni profesor')

    def mostrar_profesores(self):
        """Muestra los profesores de esta asignatura"""
        for p in self.profesores:
            print ("{} - ".format(p.nombre), end="")


    def __str__(self):

        salida=''
        salida += 'nombre: '+ self.nombre
        salida += str(self.creditos)
        salida += ', (Profesores: '
        salida += ' '.join([str(p) for p in self.profesores]) + ')'
        salida += ', (Alumnos: '
        salida += ' '.join([str(p) for p in self.alumnos]) + ')'
        return salida





#----------------------------------------------------------------------------------------