from main import Universidad

upct = Universidad("UPCT")
dep1 = upct.add_departamento("DIIC")
dep2 = upct.add_departamento("DAS")
isabel = upct.add_alumno("dnisa", "isabel", "su calle", "Femenino")
pisabel = upct.add_profesor("dnisa", "pisabel", "su calle", "Femenino", dep1)
poo = upct.add_asignatura("POO")

upct.asignar_persona_asignatura(isabel, poo)
upct.asignar_persona_asignatura(isabel, poo)
upct.desasignar_persona_asignatura(pisabel, poo)
upct.asignar_persona_asignatura(pisabel, poo) 

print(poo)
print("isabel",isabel)
upct.borrar(isabel)
print("isabel",isabel)
upct.desasignar_persona_asignatura(pisabel, poo)
print(poo)
upct.mostrar_departametos()
upct.mostrar_asignaturas()