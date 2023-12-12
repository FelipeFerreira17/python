# Risando string
# String começa a contar do zero. Estudando python a posição zero é o "E", a 1 é "S" e assim por diante.
frase = 'Estudando python'

# Fatiar
print(frase[2]) # Posição dois é T. 
print(frase[5]) # Posição cinco é A.
print(frase[2:10]) # Da posição dois ate a 9. O numero depois do dois pontos vai mostrar o anterior. 
print(frase[1:7]) # Da posição 1 até a 6. 
print(frase[:6]) # Quando não tem nenhum número antes do dois pontos, começa a mostrar a posição zero.
print(frase[8:]) # Quanto não tem nenhum numero depois do dois pontos, vai do que tá antes dos dois pontos ao final.
print(frase[4:9:2]) # Da posição 4 até a 8 pulando de dois em dois.
print(frase[:12:3]) # Da posição zero até a 11 pulando de 3 em 3.
print(frase[::2]) # Do inicio até o final pulando de 2 em 2.
print(frase.count('o')) # count conta quantas vezes algo aparece. nesse caso o "o" minusculo
print(frase.count('E')) # mostra quanta vezes o "E" maiusculo aparece.
print(frase.upper()) # upper() transforma em maiusculo.
print(frase.upper().count('A')) # Transma em maiuscula e conta quantas vezes aparece a ketra "A" maiuscula.
print(len(frase)) # len() mostra o tamanho da string.
print(len(frase.strip())) # mostra o tamanho da string e o strip() remove os espaços indesejados antes e depois.
print(frase.replace('python','android')) # replace() troca uma palavra pela outra. Mas não vai salvar. só altera nessa parte.
frase = frase.replace('python','programação') # atribuindo, ai sim faz a alteração na raiz.
print(frase)
print(frase.find('estudando')) # find() procura uma palavra que você digitou. Senão encontrar va aparecer -1
print(frase.lower()) #lower() transforma em minuscula.
print(frase.split()) # divide a string.
dividir = frase.split()
print(dividir)
