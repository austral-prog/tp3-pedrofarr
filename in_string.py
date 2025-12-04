def ejercicio1():
    nombre = input()
    nombre_minusculas = nombre.lower()
    
    print(f"Contiene a: {'a' in nombre_minusculas}")
    print(f"Contiene e: {'e' in nombre_minusculas}")
    print(f"Contiene i: {'i' in nombre_minusculas}")
    print(f"Contiene o: {'o' in nombre_minusculas}")
    print(f"Contiene u: {'u' in nombre_minusculas}")

if _name_ == "_main_":
    ejercicio1()