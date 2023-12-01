# Aumento de salário.

salario = float(input('Digite o valor do seu salário: '))
aumento = int(input('Digite o percentual de aumento do salário: '))
calculo = (aumento / 100) + 1
novosalario = salario * calculo
print ('Seu salário teve um aumento de %d por cento ' %(aumento))
print ('Seu novo salário é de R$ %5.2f' %(novosalario))
