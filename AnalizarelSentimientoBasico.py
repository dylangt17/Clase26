palabras_positivas = ["bien", "genial", "fantástico", "excelente", "feliz"]
palabras_negativas = ["mal", "terrible", "horrible", "malo", "triste"]

def analizar_sentimiento(texto):
    texto = texto.lower()
    conteo_positivo = sum(palabra in texto for palabra in palabras_positivas)
    conteo_negativo = sum(palabra in texto for palabra in palabras_negativas)

    if conteo_positivo > conteo_negativo:
        return "Sentimiento positivo"
    elif conteo_negativo > conteo_positivo:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")


# Definición de palabras con ponderaciones
ponderaciones_positivas = {
    "bien": 1,
    "genial": 2,
    "fantástico": 3,
    "excelente": 3,
    "feliz": 1
}

ponderaciones_negativas = {
    "mal": 1,
    "terrible": 2,
    "horrible": 3,
    "malo": 2,
    "triste": 1
}

def analizar_sentimiento(texto):
    texto = texto.lower()
    
    puntuacion_positiva = sum(ponderaciones_positivas.get(palabra, 0) for palabra in ponderaciones_positivas if palabra in texto)
    puntuacion_negativa = sum(ponderaciones_negativas.get(palabra, 0) for palabra in ponderaciones_negativas if palabra in texto)

    if puntuacion_positiva > puntuacion_negativa:
        return "Sentimiento positivo"
    elif puntuacion_negativa > puntuacion_positiva:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")
