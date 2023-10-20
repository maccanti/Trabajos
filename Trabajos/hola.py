Temperatura=[]
Humedad=[]
Presion:[]
with open("datos.txt","r") as hola :
    for x in hola:
         temperaturas = float(x)
         Temperatura.append(temperaturas)
    for y in hola:
         humedades = int(y)
         Humedad.append(humedades)
    for z in hola:
        presiones = float(z)
        Presion.append(presiones)
         


temperatura_promedio = sum(Temperatura) / len(Temperatura)
humedad_promedio = sum(humedades) / len(humedades)
presion_promedio = sum(presiones) / len(presiones)
print(f"Temperatura promedio: {temperatura_promedio:.1f}°C")
print(f"Humedad promedio: {humedad_promedio:.1f}%")
print(f"Presión promedio: {presion_promedio:.1f}")

#a