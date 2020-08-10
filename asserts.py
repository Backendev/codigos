def primera_letra(lista_de_palabras):
    primeras_letras = []
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es string'
        assert len(palabra) > 0, 'No se permiten cadenas vacias'
        assert palabra == "edward", "no se permite la palabra edward" 

        primeras_letras.append(palabra[0])
    return primeras_letras

print(primera_letra(["pedro","edward"]))
