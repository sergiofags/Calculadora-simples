# Calculadora simples com 4 Operações.

# Definir adição
def adicao(x, y):
    return x + y

# Definir subtração
def subtracao(x, y):
    return x - y

# Definir multiplicação
def multiplicacao(x, y):
    return x * y

# Definir divisão
def divisao(x, y):
    return x / y

# Exibir os comandos na tela para o usuário
print('Selecione a Operação:');
print('1 - Adição');
print('2 - Subtração');
print('3 - Multiplicação');
print('4 - Divisão');

while True:

# Coletar a operação digitada
    escolha = input('Escolha a operação (1/2/3/4): ')

    #Checar se foi escolhido um número válido das operações
    if escolha in ('1', '2', '3', '4'):
        try:
            #Pedir para o usuário digitar os valores
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
        except ValueError:
            #Caso digite um caracter que não seja numerico
            print("ERROR!")
            continue

    #Se for adição
    if escolha == '1':
        print(num1, "+", num2, "=", adicao(num1, num2))

    #Se for subtração
    elif escolha == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))

    #Se for multiplicação
    elif escolha == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))

    #Se for divisão
    elif escolha == '4':
        print((num1, "/", num2, "=", divisao(num1, num2)))

    #Perguntar se o usuário deseja fazer um novo calculo
    next_calculation = input("Deseja fazer outro calculo? (s/n)")
    if next_calculation == "n":
        print("Calculo Finalizado")
        break
    else:
        print("Novo Calculo")