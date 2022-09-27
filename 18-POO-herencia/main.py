import clases

persona = clases.Persona()
persona.setNombre("Jonatan")
persona.setApellido("Arez")
persona.setAltura("180cm")
persona.setEdad("700 años")

print(persona.hablar())
print(f"La persona es : {persona.getNombre()} {persona.getApellido()}")
