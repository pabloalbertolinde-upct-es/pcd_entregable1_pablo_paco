from main import Universidad

#este archivo pretende mostrar todas las funciones disponibles

#UPCT

upct = Universidad("UPCT")

#Departamentos

dep1, dep2, dep3 = upct.add_departamentos()

#Profesores

p_manuel = upct.add_profesor("dni manuel", "manuel", "calle manuel", "Masculino", dep2)
p_bea = upct.add_profesor("dnibea", "bea", "calle bea", "Femenino", dep2)
p_jose = upct.add_profesor("dnibea", "jose", "calle jose", "Masculino", dep3)

#Investigadores

i_julio = upct.add_profesor("dni julio", "julio", "calle julio", "Masculino", dep2, "señales y sistemas")
i_paco = upct.add_profesor("dni paco", "paco", "calle paco", "Masculino", dep1, "ml")
i_david = upct.add_profesor("dni david", "david", "calle david", "Masculino", dep2, "señales y sistemas")
i_isabel = upct.add_profesor("dnisa", "isabel", "su calle", "Femenino", dep1, "Astronomia")

#Asignaturas

Matematicas = upct.add_asignatura("Matematicas")
Sistemas = upct.add_asignatura("Sistemas")
ml = upct.add_asignatura("ml")
programacion = upct.add_asignatura("Programacion")

#Alumnos

esteban = upct.add_alumno("dni esteban", "esteban", "calle esteban", "Masculino")
agueda = upct.add_alumno("dni agueda", "agueda", "calle agueda", "Femenino")
fina = upct.add_alumno("dni fina", "fina", "calle fina", "Femenino")
isabel = upct.add_alumno("dni isabel", "isabel", "calle isabel", "Femenino")
luis = upct.add_alumno("dni luis", "luis", "calle luis", "Masculino")
lucas = upct.add_alumno("dni lucas", "lucas", "calle lucas", "Masculino")
mario = upct.add_alumno("dni mario", "mario", "calle mario", "Masculino")
pablo = upct.add_alumno("dni pablo", "pablo", "calle pablo", "Masculino")
paco = upct.add_alumno("dni paco", "paco", "calle paco", "Masculino")

#Asignaciones de asignaturas a los alumnos

#Matematicas
upct.asignar_persona_asignatura(esteban, Matematicas) 
upct.asignar_persona_asignatura(agueda, Matematicas) 
upct.asignar_persona_asignatura(fina, Matematicas) 
upct.asignar_persona_asignatura(isabel, Matematicas) 
upct.asignar_persona_asignatura(luis, Matematicas) 
upct.asignar_persona_asignatura(lucas, Matematicas) 
upct.asignar_persona_asignatura(mario, Matematicas) 
upct.asignar_persona_asignatura(pablo, Matematicas)
upct.asignar_persona_asignatura(paco, Matematicas)

#Sistemas
upct.asignar_persona_asignatura(esteban, Sistemas) 
upct.asignar_persona_asignatura(agueda, Sistemas) 
upct.asignar_persona_asignatura(lucas, Sistemas) 
upct.asignar_persona_asignatura(mario, Sistemas) 
upct.asignar_persona_asignatura(pablo, Sistemas)
upct.asignar_persona_asignatura(paco, Sistemas)

#ml
upct.asignar_persona_asignatura(fina, ml) 
upct.asignar_persona_asignatura(isabel, ml) 
upct.asignar_persona_asignatura(luis, ml) 
upct.asignar_persona_asignatura(lucas, ml) 
upct.asignar_persona_asignatura(pablo, ml)
upct.asignar_persona_asignatura(paco, ml)

#programacion
upct.asignar_persona_asignatura(esteban, programacion) 
upct.asignar_persona_asignatura(agueda, programacion) 
upct.asignar_persona_asignatura(fina, programacion) 
upct.asignar_persona_asignatura(isabel, programacion) 
upct.asignar_persona_asignatura(luis, programacion) 
upct.asignar_persona_asignatura(lucas, programacion) 
upct.asignar_persona_asignatura(mario, programacion) 
upct.asignar_persona_asignatura(pablo, programacion)
upct.asignar_persona_asignatura(paco, programacion)

#Asignaciones de asignaturas a los profesores e investigadores

upct.asignar_persona_asignatura(i_isabel, Matematicas)
upct.asignar_persona_asignatura(i_paco, Matematicas)
upct.asignar_persona_asignatura(i_julio, Sistemas) 
upct.asignar_persona_asignatura(i_david, Sistemas) 
upct.asignar_persona_asignatura(i_paco, ml) 
upct.asignar_persona_asignatura(p_manuel, ml) 
upct.asignar_persona_asignatura(i_julio, ml) 
upct.asignar_persona_asignatura(p_jose, programacion) 
upct.asignar_persona_asignatura(p_bea, programacion) 
upct.asignar_persona_asignatura(i_paco, programacion) 
upct.asignar_persona_asignatura(p_jose, ml)

print("Imprimiremos por pantalla algunas de las instancias para comprobar que se han creado correctamente:\n")
print(Matematicas,"\n")
print(programacion,"\n")
print(i_isabel,"\n")
print(p_jose,"\n")
print(esteban,"\n")
print(lucas,"\n")
print(agueda,"\n")
print(dep1,"\n")
print(dep3,"\n")

#Estado de la universidad

print("\n",upct,"\n")
upct.mostrar_departametos()
print("\n")
upct.mostrar_profesores()
print("\n")
upct.mostrar_alumnos()
print("\n")
upct.mostrar_asignaturas()
print("\n\n")

#Nótese que en la práctica los métodos que no son de la clase universidad no serán usados por el usuario final,
#de aquí en adelante se hace uso de ellos meramente para demostrar el correcto funcionamiento del sistema.

#Desasignar personas de asignaturas
print("Quitemos por ejemplo gente de Matematicas y programacion, empezando por los profesores isabel y jose:\n")
print("Antes:\n")
print(Matematicas.mostrar_profesores()) 
print("\n")
print(programacion.mostrar_profesores())
print("\n")
upct.desasignar_persona_asignatura(i_isabel, Matematicas)
print("\n")
upct.desasignar_persona_asignatura(p_jose, programacion)

print("\nDespués:\n")
print(Matematicas.mostrar_profesores())
print(programacion.mostrar_profesores())
print("\n\nQuitemos ahora alumnos de Matematicas (esteban y lucas) y programacion (agueda y lucas):\n")
print("Antes:\n")
print(Matematicas.mostrar_alumnos())
print("\n")
print(programacion.mostrar_alumnos())
print("\n")
upct.desasignar_persona_asignatura(esteban, Matematicas)
upct.desasignar_persona_asignatura(lucas, Matematicas)
upct.desasignar_persona_asignatura(agueda, programacion)
upct.desasignar_persona_asignatura(lucas, programacion)
print("\nDespués:\n")
print(Matematicas.mostrar_alumnos())
print("\n")
print(programacion.mostrar_alumnos())

#Aprobar asignaturas
print("\nPablo aprueba Matematicas y Sistemas:\n")
print("Antes:\n")
print(pablo)
upct.alumno_aprueba_asignatura(pablo, Matematicas)
upct.alumno_aprueba_asignatura(pablo, Sistemas)
print("\nDespués:\n")
print(pablo)
print("\n")
print(pablo.mostrar_asignaturas_aprobadas())

#Cambio de departamento y area de investigación
print("\nCambiemos a Isabel de departamento y de área de investigación:\n")
print("Antes:\n")
print(i_isabel)
print("\n")
print(dep1)
print("\n")
print(dep3)
upct.cambiar_profesor_dep(i_isabel, dep3)
upct.cambiar_investigador_area(i_isabel, "materiales")
print("\nDespués:\n")
print(i_isabel)
print(dep1)
print(dep3)

#Borrar personas
print("\nBorremos al alumno Paco, que está matriculado de todas las asignaturas:\n")
print("Antes:\n")
print(paco)
upct.mostrar_alumnos()
print(Matematicas.mostrar_alumnos())
print(Sistemas.mostrar_alumnos())
print(ml.mostrar_alumnos())
print(programacion.mostrar_alumnos())
upct.borrar(paco)
print("\nDespués:\n")
upct.mostrar_alumnos()
print(Matematicas.mostrar_alumnos())
print(Sistemas.mostrar_alumnos())
print(ml.mostrar_alumnos())
print(programacion.mostrar_alumnos())
print("\nBorremos ahora al investigador Julio, que imparte ml y sistemas y está en el dep2:\n")
print("Antes:\n")
print(dep2)
print(ml.mostrar_profesores())
print(Sistemas.mostrar_profesores())
print(i_julio)
upct.borrar(dep2) #Dirá que no se puede.
upct.borrar(i_julio)
print("\nDespués:\n")
print(dep2)
print(ml.mostrar_profesores())
print(Sistemas.mostrar_profesores())

#Estado de la universidad tras las operaciones

print(upct)
upct.mostrar_departametos()
upct.mostrar_profesores()
upct.mostrar_alumnos()
upct.mostrar_asignaturas()