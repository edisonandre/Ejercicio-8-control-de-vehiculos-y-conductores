# Listas iniciales
conductores = ["Laura", "Mateo", "Julián"]
vehiculos = ["Moto", "Carro", "Bicicleta"]

# 1. Si "Julián" está en conductores, añade "Santiago"
if "Julián" in conductores:
    conductores.append("Santiago")
    print(conductores)
    
print()

# 2. Si "Carro" está en vehiculos, añade "Camioneta"
if "Carro" in vehiculos:
    vehiculos.append("Camioneta")
    print(vehiculos)
    
print()

# 3. Si "Mateo" está en conductores, eliminarlo
if "Mateo" in conductores:
    conductores.remove("Mateo")
    print(conductores)
    
print()

# 4. Si hay más de 3 elementos en vehiculos, eliminar el primero
if len(vehiculos) > 3:
    vehiculos.pop(0) # elimina el primer elemento
    print(vehiculos)
    
print()

# 5. Si "Laura" está en conductores, reemplazarla por "Luisa"
if "Laura" in conductores:
    conductores.remove("Laura")
    conductores.append("Luisa")
    conductores.sort()
    print(conductores)
    
print()

# 6. Crear lista habilitados con los dos primeros elementos de conductores
habilitados = conductores[:2]
print(habilitados)

print()
# 7. Crear lista movilidad con los dos últimos elementos de vehiculos
movilidad = vehiculos[-2:]
print(movilidad)

print()
# 8. Si "Camioneta" está en vehiculos, crear tupla
vehiculo_extra = ()
if "Camioneta" in vehiculos:
    vehiculo_extra = ("Camioneta", "Disponible")
    print(vehiculo_extra)

print()

# 9. Si "Luisa" está en habilitados, añadir "Licencia Activa"
if "Luisa" in habilitados:
    habilitados.append("licencia activa")
    print(habilitados)
    
print()

# 10. Si "Licencia Activa" está en habilitados, crear diccionario registro

if "licencia activa" in habilitados:
    registros = {
        "conductor": "Luisa",
        "vehiculo_asignado": "Carro",
        "vigente": True
    }
    print(registros)
print()

# 11. Si existe registro, añadir "ciudad": "Bogotá"
if registros:
    registros["ciudad"] = "Bogotá"
    print(registros)

print()

# 12. Si "Bicicleta" no está en vehiculos, agregarla
if "Bicicleta" not in vehiculos:
    vehiculos.append("Bicicleta")
    print(vehiculos)

print()

# 13. Si "Julián" no está en conductores, agregarlo
if "Julián" not in conductores:
    conductores.append("Julián")
    print(conductores)
    
print()

# 14. Mostrar listas y estructuras
print("Conductores:", conductores)
print("Vehículos:", vehiculos)
print("Habilitados:", habilitados)
print("Movilidad:", movilidad)
print("Vehículo extra:", vehiculo_extra)
print("Registro:", registros)
