salario = float(input('Digite o salário: '))
base = salario
aumento = 0

if base > 1250.00:
    aumento = aumento + ((10/100) +1) 
    base = base * aumento
    print('Seu novo saário é de: %5.2f' %(base))

if base <= 1250.00:
    aumento = aumento + ((15/100)+1)
    base = base * aumento
    print('Seu novo salário é de: %5.2f' %(base))
