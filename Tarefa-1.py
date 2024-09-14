print("Bem vindo ao gerador de Sequências Fibonacci!!")

Numero = int(input("Digite um numero: ")) #numero que o usuario vai chutar para ver se é fibonacci


def gera_fibo(valor): #função para realizar a Sequência Fibonacci
    Valor = [0, 1] #Criando a Lista que ira guardar a sequência
    while len(Valor) < valor: #Verificando se o Valor é diferente do valor atual
        fibo = Valor[-1] + Valor[-2] #Adicionando o novo valor para a sequência
        Valor.append(fibo) #Adiciona um novo valor para a Lista
    for i in range (len(Valor)): #esta lendo os caracteres dentro da lista 
        if (Numero == i): ## Verificando se o Numero colocado é igual ao que você escreveu
            print ("acertou")
    return Valor
    
valor = 20 #quantidade de numeros dentro da lista

Fibonnaci = gera_fibo(valor) #guardando a função para poder chama-la
print(Fibonnaci) 

