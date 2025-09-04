
 # Programa para verificar la longitud de una palabra ingresada


palabra = input("Ingrese una palabra:")
print(f"La palabra que ingresaste es: {palabra} ")
print(f"La palabra tiene {len(palabra)} Letras")

if len(palabra) < 4: 
    faltan = 4 - len(palabra)
    print(f"Te hacen falta {faltan} letras más, debe de contener entre 4 y 8 letras, Intenta de Nuevo")
elif 4 <= len(palabra) <= 8:
    print("La palabra tiene entre 4 y 8 caracteres, Es correcta")
elif len(palabra) > 8:
    sobran = len(palabra) -8
    print(f"Te sobran {sobran} letras, Intenta de nuevo")
else:
    print("La palabra tiene más de 8 letras")

exit()