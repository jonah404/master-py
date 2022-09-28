import clases

persona = clases.Persona() #Este es el objeto
persona.setNombre("Jona")
persona.setApellido("A")
persona.setAltura("180cm")
persona.setEdad("700 años")


print(f"La persona es: {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())
print("------------------------------------------")

informatico = clases.Informatico() #Este es el objeto
informatico.setNombre("Pepe")
informatico.setApellido("X")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("------------------------------------------")

tecnico = clases.tecnicoRedes() #Objeto
tecnico.setNombre("Jose")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())


