#bibliotecas
import time
import random
import os
recordes = {} #recordes
if os.path.exists("tempos.txt"):
    with open ("tempos.txt","r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                conta = partes[0]
                tempo = float(partes[1])
                recordes[conta] = tempo
while True:
    numero1 = random.randint(2,9) #numero aleatorio 1 (entre 2 a 9)

    numero2 = random.randint(2,9) #numero aleatorio 2 (entre 2 a 9)

    multiplicacao = numero1 * numero2 #resultado certo

    inicio = time.time() #começo do cronometro

    resposta = int(input(f"{numero1}x{numero2}: ")) #resposta da pessoa

    fim = time.time() #fim do cronometro

    tempo = round(fim - inicio, 3) #quantidade de tempo levado

    #verificador da resposta
    if resposta == numero1 * numero2:
        print(f"acertou! {tempo}s")
    else:
        print(f"errou! {multiplicacao}")

    if resposta == numero1 * numero2:
        chave = f"{numero1}x{numero2}"
        if chave not in recordes or tempo < recordes[chave]:
            recordes[chave] = tempo
            print(f"Novo recorde! {tempo}s")
            with open ("tempos.txt", "w" ) as arquivo:
                for conta, t in recordes.items():
                    arquivo.write(f"{conta}:{t}\n")
        else:
            print(f"Acertou! mais falta melhorar. {recordes[chave]}s")





            