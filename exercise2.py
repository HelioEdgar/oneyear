numero = int(input("Digite um numero: "))
resultado = 0

for i in range(1, 13):
    resultado = i * numero
    print(f"{i} * {numero} = {resultado}")
    print("========== Versão 4=============")