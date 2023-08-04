grados_fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))

def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

print("La temperatura", grados_fahrenheit, "grados Fahrenheit es equivalente a", fahrenheit_a_celsius, "grados Celsius.")