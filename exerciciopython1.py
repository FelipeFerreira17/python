# Desconto mercadoria

produto = float(input('Digite o valor do produto: '))
desconto = int(input('Digite o percentual de desconto: '))
calculo = produto * (desconto / 100)
valordesconto = produto - calculo
print('O valor do desconto é de: R$ %5.2f' %(calculo))
print ('O valor a pagar com desconto é de R$ %5.2f' %(valordesconto))
