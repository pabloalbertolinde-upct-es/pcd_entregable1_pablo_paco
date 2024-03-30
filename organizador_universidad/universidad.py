from main import Universidad

upct = Universidad("UPCT")
dep1, dep2, dep3 = upct.add_departamentos()
isabel = upct.add_alumno("dnisa", "isabel", "su calle", "Femenino")
pisabel = upct.add_profesor("dnisa", "pisabel", "su calle", "Femenino", dep1)
manuel = upct.add_profesor("dnimanue", "manuel", "calle manue", "macho", dep2, "ondas")
poo = upct.add_asignatura("POO")

upct.asignar_persona_asignatura(isabel, poo)
upct.asignar_persona_asignatura(pisabel, poo) 

print(dep1)
print(pisabel)
upct.cambiar_profesor_dep(pisabel, dep2)
print(pisabel)
print(dep2)
print(dep1)
upct.cambiar_profesor_dep(pisabel, manuel)
print(pisabel)
print(dep2)
print(pisabel.mostrar_asignaturas_persona())