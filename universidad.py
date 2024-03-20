class Persona:
        def __init__(self, dni, nombre, direccion, sexo):
            self.dni = dni
            self.nombre = nombre
            self.direccion = direccion
            self.sexo = sexo
            self.asignaturas_asignadas=[]

        def asesinar(self):

            # hay que quitar a todos los alumnos y profesores de todas las asignaturas,
            # ademas de borrar toda su informacion

            pass

        def asignar(self, asignatura):
            asignatura.añadir(self)
            self.asignaturas_asignadas.append(asignatura)

        def quit(self, asignatura):
            asignatura.quitar(self)

        def nombre_persona(self):
            return str(self.nombre)

#-----------------------------------------------


class Alumno(Persona):
    def __init__(self, dni, nombre, direccion, sexo):
        Persona.__init__(self, dni, nombre, direccion, sexo)













#-----------------------------------------------

class Titular(Persona):

    def __init__(self, dni, nombre, direccion, sexo, area):
        Persona.__init__(self, dni, nombre, direccion, sexo)
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

    #def agregar_profesor(self, profesor):
    #    """Agrega un profesor a la lista de profesores"""
    #    if isinstance(profesor, Profesor):
    #        self.profesores.append(profesor)
    #    else:
    #        raise TypeError('El objeto no es una instancia de la clase Profesor')
    #
    #def matricular_alumno(self, alumno):
    #    """Agrega un profesor a la lista de profesores"""
    #    if isinstance(alumno, Alumno):
    #        self.alumnos.append(alumno)
    #    else:
    #        raise TypeError('El objeto no es una instancia de la clase Alumno')

    def quitar(self, persona):
        """Agrega un profesor o alumno a la asignatura"""
        if isinstance(persona, Alumno) and persona in self.alumnos:
            self.alumnos.remove(persona)

        elif isinstance(persona, Profesor) and persona in self.profesores:
            self.profesores.remove(persona)

        else:
            raise TypeError('El objeto no es una instancia de la clase Alumno ni profesor')

    #def quitar_profesor(self, profesor):
    #    """Quita un profesor de la lista de profesores"""
    #
    #    self.profesores.remove(profesor)
#
    #def quitar_alumno(self, alumno):
    #    """Quita un profesor de la lista de profesores"""
    #
    #    self.profesores.remove(alumno)


    def mostrar_profesores(self):
        """Muestra los profesores de esta asignatura"""
        a='los profesores de esta asignatura son:'
        for p in self.profesores:
            a += '\n'
            a += p.nombre_persona()

        return a

    def mostrar_alumnos(self):
        """Muestra los alumnos de esta asignatura"""
        a='los alumnos matriculados son:'
        for p in self.alumnos:
            a += '\n'
            a += p.nombre_persona()
        return a

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


# Creamos algunas instancias de Profesor, Alumno y Asignatura
pjuan = Profesor("12345678A", "Juan", "Calle Principal 123", "Masculino")
pmaria = Profesor("87654321B", "María", "Avenida Central 456", "Femenino")
pjose = Profesor("noseque", "jose", "calle su casa", "Masculino")
pdavid = Profesor("nosecual", "david", "Avenida la casa 456", "Femenino")
profesora_isabel = Profesor("dnisa", "isabel", "su calle", "Femenino")

pedro = Alumno("11111111X", "Pedro", "Calle Secundaria 321", "Masculino")
ana = Alumno("22222222Y", "Ana", "Plaza Principal 789", "Femenino")
julian = Alumno("55555555X", "julian", "Calle Secundaria 321", "Masculino")
paco = Alumno("48838889E", "paco", "Plaza Principal 789", "Masculino")
pablo = Alumno("00000000Z","pablo","calle alhambra","Masculino")


mates = Asignatura("Matemáticas")
historia = Asignatura("Historia")
calculo1 = Asignatura("Calculo1")
Literatura = Asignatura("Literatura")

# Asignamos profesores y alumnos a las asignaturas
mates.añadir(pjuan)
mates.añadir(pedro)

historia.añadir(pmaria)
historia.añadir(ana)

pablo.asignar(calculo1)
pablo.asesinar()

julian.asignar(historia)
pdavid.asignar(mates)
paco.asignar(historia)

profesora_isabel.asignar(Literatura)
paco.asignar(Literatura)

# Mostramos los profesores y alumnos de cada asignatura

print(mates.mostrar_profesores())


print(historia.mostrar_profesores())


print(mates.mostrar_alumnos())


print(historia.mostrar_alumnos())

julian.quit(historia)
pdavid.quit(mates)


# Mostramos los profesores y alumnos de cada asignatura

print(mates.mostrar_profesores())

print(historia.mostrar_profesores())

print(mates.mostrar_alumnos())

print(historia.mostrar_alumnos())


print(calculo1.mostrar_alumnos())


