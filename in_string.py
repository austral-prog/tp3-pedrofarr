def verificar_vocales_en_nombre(nombre):
    nombre_minusculas = nombre.lower()
    contiene_a = 'a' in nombre_minusculas
    contiene_e = 'e' in nombre_minusculas
    contiene_i = 'i' in nombre_minusculas
    contiene_o = 'o' in nombre_minusculas
    contiene_u = 'u' in nombre_minusculas
    
    print(f"Contiene a: {contiene_a}")
    print(f"Contiene e: {contiene_e}")
    print(f"Contiene i: {contiene_i}")
    print(f"Contiene o: {contiene_o}")
    print(f"Contiene u: {contiene_u}")
# verificar_vocals_en_nombre()