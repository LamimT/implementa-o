def lados_proporcionais(lados1, lados2):
    # Verifica se os lados são proporcionais
    proporcao = lados1[0] / lados2[0]
    return all(round(lados1[i] / lados2[i], 5) == round(proporcao, 5) for i in range(1, len(lados1)))

def verificar_LAL(lados1, angulo1, lados2, angulo2):
    # Verifica se dois lados são proporcionais e o ângulo entre eles é congruente
    if round(angulo1, 5) == round(angulo2, 5):
        return lados_proporcionais([lados1[0], lados1[1]], [lados2[0], lados2[1]])
    return False

def verificar_AA(angulos1, angulos2):
    # Verifica se dois ângulos são congruentes
    angulos1_ordenados = sorted(angulos1)
    angulos2_ordenados = sorted(angulos2)
    return round(angulos1_ordenados[0], 5) == round(angulos2_ordenados[0], 5) and \
           round(angulos1_ordenados[1], 5) == round(angulos2_ordenados[1], 5)

def verificar_LLL(lados1, lados2):
    # Verifica se todos os lados são proporcionais
    return lados_proporcionais(lados1, lados2)

def verificar_semequencia(triangulo1, triangulo2):
    resultado = ""
    verificou = False

    # Verificar LAL
    if 'lados' in triangulo1 and 'angulo' in triangulo1:
        if verificar_LAL(triangulo1['lados'], triangulo1['angulo'], triangulo2['lados'], triangulo2['angulo']):
            resultado += "Triangulos sao semelhantes pelo criterio LAL: Dois lados proporcionais e o angulo entre eles congruente.\n"
            verificou = True
        else:
            resultado += "Os triangulos NAO sao semelhantes pelo criterio LAL.\n"

    # Verificar AA (se houver ângulos fornecidos)
    if 'angulos' in triangulo1 and 'angulos' in triangulo2:
        if verificar_AA(triangulo1['angulos'], triangulo2['angulos']):
            resultado += "Triangulos sao semelhantes pelo criterio AA: Dois angulos congruentes.\n"
            verificou = True
        else:
            resultado += "Os triangulos NAO sao semelhantes pelo criterio AA: Dois angulos NAO sao congruentes.\n"

    # Verificar LLL (se houver lados fornecidos)
    if 'lados' in triangulo1 and 'lados' in triangulo2:
        if verificar_LLL(triangulo1['lados'], triangulo2['lados']):
            resultado += "Triangulos sao semelhantes pelo criterio LLL: Todos os lados proporcionais.\n"
            verificou = True
        else:
            resultado += "Os triangulos NAO sao semelhantes pelo criterio LLL: Os lados NAO sao proporcionais.\n"

    if not verificou:
        return "Os triangulos nao sao semelhantes por nenhum criterio."
    return resultado

# Exemplo de uso com apenas dois triângulos (já ditos):

# Triângulos dados pelos lados e ângulos para LAL
triangulo1 = {'lados': [3, 5], 'angulo': 72.5}
triangulo2 = {'lados': [6, 10], 'angulo': 72.5}

resultado = verificar_semequencia(triangulo1, triangulo2)
print(resultado)

# Outro exemplo com ângulos (AA) ou lados (LLL)
