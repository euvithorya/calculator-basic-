def mostrar_menu():
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero."

def obter_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def calculadora():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma operação (1/2/3/4) ou 'q' para sair: ")

        if escolha == 'q':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha in ['1', '2', '3', '4']:
            num1, num2 = obter_numeros()

            if escolha == '1':
                print(f"Resultado: {adicao(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {divisao(num1, num2)}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()
