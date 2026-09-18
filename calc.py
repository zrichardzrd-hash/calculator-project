# Pede os número para usuário 
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número"))

#   Verificar qual foi a operação escolhida e faz o cálculo
if  operacao == '+':
    resultado = num1 + num2
elif operacao ==  '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
        if num2 !=  0:
            resultado = num1 / num2
        else:
            resultado = "Erro:  Não é possível dividir por zero!"
else: 
    resultado = "Operação invalida"

#   Mostra o resultado na tela 
print(f"O resultado é: {resultado}")
