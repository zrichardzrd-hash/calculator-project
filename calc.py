def calculate(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Não é possível dividir por zero!"
    elif operacao == "**":
        return num1 ** num2
    elif operacao == '%':
        return num1 % num2
    else:
        return "Operação inválida"
while True:
    # Pede os número para usuário 
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /, **, %): ")
    num2 = float(input("Digite o segundo número"))

    # Chama a função de cálculo
    resultado = calculate(num1, num2, operacao)

    #   Mostra o resultado na tela 
    print(f"O resultado é: {resultado}")
    # Salva o histórico no arquivo
    with open("historico.txt", "a") as arquivo:
        arquivo.write(f"{num1} {operacao} {num2} = {resultado}\n")
    # Pergunta se o usuário quer continuar
    continuar = input("Deseja fazer outra opeação? (s/n): ")

    if continuar.lower() != 's':
        print("Encerrando a calculadora; Até logo!")
        break