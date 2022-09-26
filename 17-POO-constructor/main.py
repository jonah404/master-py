from coche import Coche

carro = Coche("Rojo", "Lamborghini", "Aventador", 300, 500, 2)
carro1 = Coche("Gris", "Mercedes Benz", "AMG GT S", 300, 500, 2)
carro2 = Coche("Negro", "BMW", "430i", 300, 500, 2)
carro3 = Coche("Azul", "Pagani", "Zonda", 300, 500, 2)


print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado (Hay que compararlo con la clase)

if type(carro3) == Coche:
    print("Es un objeto correcto!")
else:
    print("No es un objeto")

# Visibilidad

print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())
