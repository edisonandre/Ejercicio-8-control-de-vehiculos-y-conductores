conductores = ["Laura", "Mateo", "Julian"]
vehiculos = ["Moto", "Carro", "Bicicleta"]


if conductores[2] == "Julian":
    conductores.append("Santiago")
    print(conductores)
    
print()
    
if vehiculos[1] == "Carro":
    vehiculos.append("Camioneta")
    print(vehiculos)
print("")
    
if conductores[1] == "Mateo":
    conductores.remove("Mateo")
    print(conductores)
    
print()
    
if len(vehiculos) > 3:
    vehiculos.remove(vehiculos[0])
    print(vehiculos)
    
print()

if conductores[0] == "Laura":
    conductores[0].remove("Laura")
    conductores.append("Luisa")
    conductores.sort()
    print(conductores)

print()

habilitados = [conductores[0], conductores[1]]
movilidad = [vehiculos[0], vehiculos[1]]

if vehiculos[2] == "Camioneta":
    vehiculos_extra = ("Camioneta", "Disponible")
    print(vehiculos_extra)
    
print()
    
if habilitados[1] == "Luisa":
    habilitados.append("Licencia Activa")
    print(habilitados)
    
print()

if habilitados[2] == "Licencia Activa":
    registro = {
        "conductor": "Luisa",
        "Vehiculo_asignado": "Carror",
        "vigente": "True"
    }
    print(registro)
print()

if registro == registro:
    registro["ciudad"] = "bogota"
    print(registro)

print(vehiculos)

print(conductores)
print(vehiculos)
print(habilitados)
print(movilidad)
print(registro)