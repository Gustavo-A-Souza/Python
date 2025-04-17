import math

def verificar_triangulo(lado1, lado2, lado3):
    # Verifica se os lados podem formar um triângulo
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Não é um triângulo"
    
    # Ordena os lados para garantir que lado3 seja o maior
    lados = sorted([lado1, lado2, lado3])
    
    # Verifica se a soma dos dois menores lados é maior que o maior lado
    if lados[0] + lados[1] > lados[2]:
        # Verifica se é um triângulo retângulo (Teorema de Pitágoras)
        if math.isclose(lados[0]**2 + lados[1]**2, lados[2]**2):
            if lados[0] == lados[1] == lados[2]:
                return "É um triângulo: equilátero retângulo"
            elif lados[0] == lados[1] or lados[1] == lados[2]:
                return "É um triângulo: isósceles retângulo"
            else:
                return "É um triângulo: escaleno retângulo"
        else:
            # Triângulo não retângulo
            if lados[0] == lados[1] == lados[2]:
                return "É um triângulo: equilátero não retângulo"
            elif lados[0] == lados[1] or lados[1] == lados[2]:
                return "É um triângulo: isósceles não retângulo"
            else:
                return "É um triângulo: escaleno não retângulo"
    else:
        return "Não é um triângulo"

# Função principal para testar a função verificar_triangulo
def main():
    lado1 = float(input("Digite o primeiro lado: "))
    lado2 = float(input("Digite o segundo lado: "))
    lado3 = float(input("Digite o terceiro lado: "))
    
    resultado = verificar_triangulo(lado1, lado2, lado3)
    print(resultado)

# Chama a função principal
main()