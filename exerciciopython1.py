#Pintura da parede
largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de %1.1f X %1.2f e sua área é de %1.3f m²' %(largura,altura,area))
print('Para pintar essa parede, você precisará de %f L de tinta.' % (tinta))