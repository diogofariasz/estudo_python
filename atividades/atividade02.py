#atividade01
print("É preciso fazer todos os algoritmos", 
      "para aprender Python!!")

#atividade 02
ifrn = "Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte"
print(ifrn)

#atividade 03
numero = int(input("Digite um número: "))
print("o numero é:", numero)

#atividade 04
valor = float(input("digite um numero: "))
numero = valor * 2

print(f"o dobro é: {numero:.2f}")

#atividade 05
numerador = int(input("digite um numero: "))
denominador = int(input("digite um numero: "))

fracao = numerador / denominador
print(f"o numero é: {fracao:.2f}")

#atividade 06
peso = float(input("digite um numero: "))
altura = float(input("digite um numero: "))

imc= peso / (altura*2)
print(f"seu imc é: {imc:.2f}")

#atividade 07
nota1 = float(input("digite um numero: "))
nota2 = float(input("digite um numero: "))
nota3 = float(input("digite um numero: "))

media = (nota1 + nota2 + nota3) / 3
print(f"a média é: {media:.2f}")

#atividade 08
valor = float(input("digite um numero: "))
resultado = valor * 0.15

print(f"o valor é: {resultado:.2f}")

#atividade 09
venda = float(input("Digite o valor do produto: "))

desconto = valor * 0.15
resultado = valor - desconto

print(f"o valor é: R$ {resultado:.2f}")

#atividade 10
salario_minimo = 1.518
seu_salario = float(input("Digite o valor do seu salário: "))

valor = seu_salario / salario_minimo
print(f"Você recebe: R$  {valor:.2f} salários mínimos.")