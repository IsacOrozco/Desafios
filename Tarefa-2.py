Palavra = input("Entre com um texto:").upper()## upper é para tudo que entrar ser maiusculo, e verificar todos os A
achar = 'A'
letra = []
numero = 0
total = 0
while achar in Palavra:     #Enquanto estiver tendo a palavra A, ele continuara procurando
  busca = Palavra.find(achar) #acha a posicao correta da onde esta o A
  letra.append(busca+total) #inclui posição a posição da palavra dentro da lista
  Palavra = Palavra[(busca+1):]    #remove todas as palavras menos o A
  total = total + busca + 1 #esta somando a quantidade de vezes que aparece na tela
  for i in range (len(letra)): #buscando dentro da lista todas os caracteres A dentro: obs: tudo é a na lista
    if (numero == i): 
        numero = numero + 1 #adiciona 1 ponto a cada caracter na lista
        
print(numero)   

