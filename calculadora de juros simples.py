# Apresentação da calculadora

# multiplicação


print('\n\t\t\t -- calculadora de juros simples __\n')

# entrada
n1 = float(input('informe o capital:'))
n2 = float(input('informe a taxa:'))
n3 = float(input('informe o prazo '))

#processamento

q = n1*n2*n3
total= q//100

#saida
print(f' o valor do juros é de -- {total} --')