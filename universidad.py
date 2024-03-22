class Persona:

    def __init__(self, dni, nombre, direccion, sexo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.sexo = sexo
        self.asignaturas_asignadas=[]

    def abandona_universidad(self):
        """
        Desasigna a la persona de todas sus asignaturas (y departamento si es profesor).
        """
        if isinstance(self, Profesor):
            self.dep.departamento_quitar(self)
        for asignatura in self.asignaturas_asignadas:
            self.desasignar_asignatura(asignatura)

    def no_asignada(self, asignatura):   # para no duplicar personas
        return (((isinstance(self, Profesor)) and (self not in asignatura.profesores)) or
               ((isinstance(self, Alumno)) and (self not in asignatura.alumnos)))

    def asignar_asignatura(self, asignatura):
        if self.no_asignada(asignatura):
            self.asignaturas_asignadas.append(asignatura)
            asignatura.asignatura_añadir(self)
        else:
            raise ValueError("La persona ya tiene asignada la asignatura")

    def desasignar_asignatura(self, asignatura):
        if not self.no_asignada(asignatura):
            self.asignaturas_asignadas.remove(asignatura)
            asignatura.asignatura_quitar(self)
        else:
            raise ValueError("La persona no tiene asignada la asignatura")

    def nombre_persona(self):
        return self.nombre

    def mostrar_asignaturas(self):
        return f"las asignaturas de {self.nombre} son: "+", ".join(str(asignatura.nombre) for asignatura in self.asignaturas_asignadas)

    def __str__(self):
        a = ''
        a += 'Nombre: '+ self.nombre
        a += ", DNI: " + self.dni
        a += ", Dirección: " + self.direccion
        a += ", Asignaturas asignadas: " + self.mostrar_asignaturas()
        if isinstance(self, Profesor):
            a += ", Departamento: " + self.dep.nombre_dep()
        if isinstance(self, Investigador):
            a += ", Area de investigación: " + self.area
        return a

#-----------------------------------------------

class Departamento:

#    departamentos = [DIS, DITEC, DIS]

    def __init__(self, nombre):
#       if nombre not in Departamento.departamentos:
#           raise ValueError("El departamento no existe. Departamentos existentes: DIIC, DITEC, DIS")
        self.nombre = nombre
        self.profesores = []

    def nombre_dep(self):
        return self.nombre

    def departamento_añadir(self, persona):
        """Agrega un profesor al departamento."""
        if isinstance(persona, Profesor) and persona not in self.profesores:
            self.profesores.append(persona)
        else:
            raise TypeError('El objeto no es una instancia de profesor o ya está en el departamento')

    def departamento_quitar(self, persona):
        """Quita un profesor del departamento."""
        if isinstance(persona, Profesor) and persona in self.profesores:
            self.profesores.remove(persona)
        else:
            raise TypeError('El objeto no es una instancia de profesor o no está en el departamento')

    def __str__(self):
        salida=''
        salida += 'Nombre: '+ self.nombre
        salida += ', (Profesores: '
        salida += ', '.join([str(p.nombre_persona()) for p in self.profesores]) + ')'
        return salida

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
#        if dep in Departamento.departamentos:
            self.dep = dep
#        else:
#            raise ValueError("El departamento no existe. \nDepartamentos existentes: DIIC, DITEC, DIS")

class Investigador(Profesor): #titulares

    def __init__(self, dni, nombre, direccion, sexo, dep, area):
        Profesor.__init__(self, dni, nombre, direccion, sexo, dep)
        self.area = area

    def cambio_area(self, area):
        self.area = area

#--------------------------------------------------------------------------------------------

class Asignatura:

    def __init__(self, nombre, creditos=6):
        '''iniciamos la clase Asignatura'''
        self.nombre = nombre  # Nombre de la asignatura
        self.creditos = creditos     # Número de créditos
        self.profesores = []   # Lista de profesores que imparten la asignatura
        self.alumnos = [] #lista de alumnos

    def asignatura_añadir(self, persona):
        """Agrega un profesor o alumno a la asignatura"""
        if isinstance(persona, Alumno):
            self.alumnos.append(persona)

        elif isinstance(persona, Profesor):
            self.profesores.append(persona)

        else:
            raise TypeError('El objeto no es una instancia de la clase Alumno ni profesor')

    def asignatura_quitar(self, persona):
        """Agrega un profesor o alumno a la asignatura"""
        if isinstance(persona, Alumno) and persona in self.alumnos:
            self.alumnos.remove(persona)

        elif isinstance(persona, Profesor) and persona in self.profesores:
            self.profesores.remove(persona)

        else:
            raise TypeError('El objeto no es una instancia de la clase Alumno ni profesor')

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
        salida += 'Nombre: '+ self.nombre
        salida += ', créditos: ' + str(self.creditos)
        salida += ', (Profesores: '
        salida += ', '.join([str(p.nombre_persona()) for p in self.profesores]) + ')'
        salida += ', (Alumnos: '
        salida += ', '.join([str(p.nombre_persona()) for p in self.alumnos]) + ')'
        return salida

#----------------------------------------------------------------------------------------

DIS = Departamento("DIS")

pjuan = Profesor("12345678A", "Juan", "Calle Principal 123", "Masculino", DIS)
pmaria = Profesor("87654321B", "María", "Avenida Central 456", "Femenino", DIS)
pjose = Profesor("noseque", "jose", "calle su casa", "Masculino", DIS)
pdavid = Profesor("nosecual", "david", "Avenida la casa 456", "Femenino", DIS)
pisabel = Profesor("dnisa", "isabel", "su calle", "Femenino", DIS)

ijuan = Investigador("12345678A", "Juan", "Calle Principal 123", "Masculino", DIS, "teleco")
imaria = Investigador("87654321B", "María", "Avenida Central 456", "Femenino", DIS, "teleco")
ijose = Investigador("noseque", "jose", "calle su casa", "Masculino", DIS, "teleco")
idavid = Investigador("nosecual", "david", "Avenida la casa 456", "Femenino", DIS, "teleco")
iisabel = Investigador("dnisa", "isabel", "su calle", "Femenino", DIS, "teleco")

apedro = Alumno("11111111X", "Pedro", "Calle Secundaria 321", "Masculino")
aana = Alumno("22222222Y", "Ana", "Plaza Principal 789", "Femenino")
ajulian = Alumno("55555555X", "julian", "Calle Secundaria 321", "Masculino")
apaco = Alumno("48838889E", "paco", "Plaza Principal 789", "Masculino")
apablo = Alumno("00000000Z","pablo","calle alhambra","M")

mates = Asignatura("Matemáticas")
historia = Asignatura("Historia")
calculo = Asignatura("Calculo")
Literatura = Asignatura("Literatura")

#----------------------------------------------------------------------------------------

#apablo.asignar_asignatura(calculo)
#apaco.asignar_asignatura(calculo)
#pjose.asignar_asignatura(calculo)
pjose.asignar_asignatura(historia)
idavid.asignar_asignatura(calculo)
#idavid.desasignar_asignatura(calculo)
#idavid.desasignar_asignatura(calculo)
idavid.asignar_asignatura(historia)

#apablo.asignar_asignatura(calculo)
#apablo.abandona_universidad()
#del apablo

#print(calculo)
#print(apablo)

#DIS.departamento_añadir(apaco)
DIS.departamento_quitar(pjose)
print(DIS)

idavid.abandona_universidad()
del idavid
print(DIS)
print(historia) # algo falla
print(pjose)