def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros)/len(numeros)
    
numeros = []

while True:
    entrada = input("Digite um numero:")
    if not entrada.isdigit():
        break
    
    numeros.append(int(entrada))
    
media = calcular_media(numeros)
print(f"a média dos numeros digitados é: {media:.2f}")