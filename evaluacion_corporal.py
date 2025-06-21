print("-------------------------------------")
print("Evaluación de peso corporal")
print("-------------------------------------")

peso = int(input("Ingrese su peso (kg): "))
estatura = float(input("Ingrese su estatura (m): "))

imc = peso / (estatura **2)

if imc < 18.5:
    print(f"Tiene bajo peso con un IMC de {imc:.1f}")
elif 18.5 <= imc <= 24.9:
    print(f"Está en un peso normal con un IMC de {imc:.1f}")
elif 25 <= imc <= 29.9:
    print(f"Tiene sobrepeso con un IMC de {imc:.1f}")
else:
    print(f"Tiene obesidad con un IMC de {imc:.1f}")