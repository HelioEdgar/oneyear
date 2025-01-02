contagem = 0
numero = 1

while True:
    if numero % 2 == 0:
        print(numero)
        contagem += 1
    numero += 1

    if contagem == 10:
        break