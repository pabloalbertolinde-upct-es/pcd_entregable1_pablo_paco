from main import Universidad

#------------UPCT

upct = Universidad("UPCT")

#---------Departamentos

dep1, dep2, dep3 = upct.add_departamentos()

#------Profesores

p_manuel = upct.add_profesor("dni manuel", "manuel", "calle manuel", "Masculino", dep2)
p_bea = upct.add_profesor("dnibea", "bea", "calle bea", "Femenino", dep2)
p_jose = upct.add_profesor("dnibea", "jose", "calle jose", "Masculino", dep3)

#------Investigadores

i_julio = upct.add_profesor("dni julio", "julio", "calle julio", "Masculino", dep2, "señales y sistemas")
i_paco = upct.add_profesor("dni paco", "paco", "calle paco", "Masculino", dep1, "Calculo")
i_david = upct.add_profesor("dni david", "david", "calle david", "Masculino", dep2, "señales y sistemas")
i_isabel = upct.add_profesor("dnisa", "isabel", "su calle", "Femenino", dep1, "Astronomia")

#------asignaturas

Matematicas = upct.add_asignatura("Matematicas")
Sistemas = upct.add_asignatura("Sistemas")
Calculo = upct.add_asignatura("Calculo")
programacion = upct.add_asignatura("Programacion")



#------Alumnos

esteban = upct.add_alumno("dni esteban", "esteban", "calle esteban", "Masculino")
agueda = upct.add_alumno("dni agueda", "agueda", "calle agueda", "Femenino")
fina = upct.add_alumno("dni fina", "fina", "calle fina", "Femenino")
isabel = upct.add_alumno("dni isabel", "isabel", "calle isabel", "Femenino")
luis = upct.add_alumno("dni luis", "luis", "calle luis", "Masculino")
lucas = upct.add_alumno("dni lucas", "lucas", "calle lucas", "Masculino")
mario = upct.add_alumno("dni mario", "mario", "calle mario", "Masculino")


#-------------------------------Asignaciones de asignaturas

#-alumnos

#matematicas
upct.asignar_persona_asignatura(esteban, Matematicas) 
upct.asignar_persona_asignatura(agueda, Matematicas) 
upct.asignar_persona_asignatura(fina, Matematicas) 
upct.asignar_persona_asignatura(isabel, Matematicas) 
upct.asignar_persona_asignatura(luis, Matematicas) 
upct.asignar_persona_asignatura(lucas, Matematicas) 
upct.asignar_persona_asignatura(mario, Matematicas) 

#Sistemas
upct.asignar_persona_asignatura(esteban, Sistemas) 
upct.asignar_persona_asignatura(agueda, Sistemas) 
upct.asignar_persona_asignatura(lucas, Sistemas) 
upct.asignar_persona_asignatura(mario, Sistemas) 

#Calculo
upct.asignar_persona_asignatura(fina, Calculo) 
upct.asignar_persona_asignatura(isabel, Calculo) 
upct.asignar_persona_asignatura(luis, Calculo) 
upct.asignar_persona_asignatura(lucas, Calculo) 

#programacion
upct.asignar_persona_asignatura(esteban, programacion) 
upct.asignar_persona_asignatura(agueda, programacion) 
upct.asignar_persona_asignatura(fina, programacion) 
upct.asignar_persona_asignatura(isabel, programacion) 
upct.asignar_persona_asignatura(luis, programacion) 
upct.asignar_persona_asignatura(lucas, programacion) 
upct.asignar_persona_asignatura(mario, programacion) 

#-profesores e investigadores

upct.asignar_persona_asignatura(i_isabel, Matematicas)
upct.asignar_persona_asignatura(i_paco, Matematicas)
upct.asignar_persona_asignatura(i_julio, Sistemas) 
upct.asignar_persona_asignatura(i_david, Sistemas) 
upct.asignar_persona_asignatura(i_paco, Calculo) 
upct.asignar_persona_asignatura(p_manuel, Calculo) 
upct.asignar_persona_asignatura(p_jose, programacion) 
upct.asignar_persona_asignatura(p_bea, programacion) 
upct.asignar_persona_asignatura(i_paco, programacion) 
upct.asignar_persona_asignatura(p_jose, Calculo) 


print(upct)

# ahora  vamos a probar los metodos para cambiar ciertas cosas

agueda.aprobar_asignatura(Matematicas)
upct.desasignar_persona_asignatura(lucas, programacion)
upct.cambiar_profesor_dep(p_bea, dep3)

upct.borrar(mario)
upct.borrar(i_paco)


print(" \n--------------------------\nsegundo print\n--------------------------")

print(upct)

print("\n\n\n")

#ahora mostraremos los profesores, los alumnos, las asignaturas y los departamentos por separado

upct.mostrar_alumnos()
upct.mostrar_asignaturas()
upct.mostrar_departametos()
upct.mostrar_profesores()

upct.asignar_persona_asignatura(i_paco, Matematicas)

print(i_paco)

