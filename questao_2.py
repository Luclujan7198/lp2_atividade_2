def contadorVogal(texto):
    
    TextoMin = texto.lower()
    vogais = ['a','e','i','o','u']
    for i in vogais:
        if i in TextoMin:
            return {i: TextoMin.count(i)}