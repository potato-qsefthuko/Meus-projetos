import math
#função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Testa ímpares de 3 até a raiz quadrada de n
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True
#função-end

# Solicita ao usuário um número e verifica se é primo.
try:
    num = int(input("Digite um número: "))
    if eh_primo(num):
        print(f"\n\n{num} é primo.\n\n")
    else:
        print(f"\n\n{num} não é primo.\n\n")
except:
    print("Por favor, digite um número inteiro válido.")