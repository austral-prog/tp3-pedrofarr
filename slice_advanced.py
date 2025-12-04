# Ejercicio 2 - Operaciones de slicing
def ejercicio2():
    texto = "Awesome"
    
    # Primera operación
    resultado1 = texto[0:3].lower()
    print(resultado1)
    
    # Segunda operación
    resultado2 = texto[2:5].lower()
    print(resultado2)
    
    # Tercera operación
    resultado3 = (texto[0:4] + texto[-3:]).lower()
    print(resultado3)

if _name_ == "_main_":
    ejercicio2()