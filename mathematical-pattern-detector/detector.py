def descobrir_padrao():
    print("--Bah meia noite e eu aq fazendo desafio ;-;--")
    
    # 1. O usuário digita a lista (ex: 3,7,11,15)
    entrada = input("Digite a lista: ")
    
    # Transformamos o texto em uma lista de números inteiros
    # O .split(',') corta o texto nas vírgulas e o int(x) transforma em número
    lista = [int(x.strip()) for x in entrada.split(',')]
    
    if len(lista) < 2:
        print("Minimo de 2 números.")
        return

    # 2. Testar se é a sequência de Quadrados Perfeitos (n²)
    e_quadrado = True
    for i in range(len(lista)):
        if lista[i] != (i + 1) ** 2:
            e_quadrado = False
            break
    
    if e_quadrado:
        print("\n Padrão detectado: Números ao Quadrado (n²)")
        pos = int(input("Qual posição você quer descobrir? "))
        print(f"O número na posição {pos} é: {pos**2}")
        return

    # 3. Testar se é uma Sequência Linear (pula de quanto em quanto)
    razao = lista[1] - lista[0]
    # Fórmula: termo = n * razao + ajuste
    # Para achar o ajuste: ajuste = primeiro_termo - razao
    ajuste = lista[0] - razao
    
    # Verificamos se a razão é a mesma na lista toda (para ter certeza)
    eh_linear = True
    for i in range(len(lista) - 1):
        if lista[i+1] - lista[i] != razao:
            eh_linear = False
            break
            
    if eh_linear:
        sinal = "+" if ajuste >= 0 else "-"
        print(f"\n✅ Padrão detectado: Sequência Linear!")
        print(f"Fórmula: {razao}n {sinal} {abs(ajuste)}")
        
        pos = int(input("Qual posição você quer descobrir? "))
        resultado = (razao * pos) + ajuste
        print(f"O número na posição {pos} é: {resultado}")
    else:
        print("\n❌ Padrão muito complexo! Esse o 'Sherlock' ainda não consegue ler.")

# Rodar o programa
descobrir_padrao()