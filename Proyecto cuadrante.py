#Encuentra el cuadrante 
import sys

EjeX = 0
EjeY = 0


CuadranteI = (1, 1)  # (+, +) 
CuadranteII = (-1, 1) # (-, +)
CuadranteIII = (-1, -1) # (-, -)
CuadranteIV = (1, -1) # (+, -)

def validar_numero(valor):
    if not valor.strip():
        print("Debes incluir un numero")
        sys.exit()

    try:  
        return int(valor) #Verifica si es un numero entero
    except ValueError:
        print("El valor ingresado no es numerico")
        sys.exit()

  
X = validar_numero(input("Ingrese el valor de X:"))
Y = validar_numero(input("Ingrese el valor de Y:"))

print(f"Tu punto es ({X}, {Y})")

# Identificamos el cuadrante

if X > 0 and Y > 0: 
    print("El punto se encuentra en el CuadranteI")

elif X < 0 and Y > 0:
    print("El punto se encuentra en el CuadranteII")

elif X < 0 and Y < 0:
    print("El punto se encuentra en el CuadranteIII")

elif X > 0 and Y < 0:
    print("El punto se encuentra en el cuadranteIV")

elif X == 0 and Y == 0:
    print("El punto se encuentra en el origen")

elif X == 0:
    print("El punto se encuentra en el eje Y")

elif Y == 0:
    print("El punto se encuentra en el eje X")
    