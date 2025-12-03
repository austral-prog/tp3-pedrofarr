def aplicar_slices(texto):
    texto_minusculas = texto.lower()
    
    primeras_tres = texto_minusculas[0:3]
    
    longitud = len(texto_minusculas)
    medio_inicio = longitud // 2 - 1
    medio_fin = medio_inicio + 3
    tres_del_medio = texto_minusculas[medio_inicio:medio_fin]
    
    primera_cuarta = texto_minusculas[0:4]
    antepenultima_ultima = texto_minusculas[-3:]
    concatenacion = primera_cuarta + antepenultima_ultima
    
    print(primeras_tres)
    print(tres_del_medio)
    print(concatenacion)