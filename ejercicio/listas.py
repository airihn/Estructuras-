def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

try:
    base = int(input("Ingresa la base (número entero): "))
    exponente = int(input("Ingresa el exponente (entero no negativo): "))
      
    if exponente < 0:
        print("El exponente debe ser un número entero no negativo.")
    else:
        resultado = potencia(base, exponente)
        print(f"{base} elevado a {exponente} es: {resultado}")
except ValueError:
    print("Por favor, ingresa solo números enteros válidos.") 