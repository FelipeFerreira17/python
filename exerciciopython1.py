# Carro alugado

dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
kms = float(input('Digite os KMs percorridos pelo carro: '))
calculo = (dias * 60) + (kms * 0.15)
print ('O valor a pagar pelo carro alugado é de: R$ %5.2F' %(calculo))
