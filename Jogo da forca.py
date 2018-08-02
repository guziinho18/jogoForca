#Gustavo Alex Torres

import urllib.request
import random    

tamanhopalavra = [] #Lista para o usuario identicar o tamanho da palavra  
certas = '' #Variavel com as letras corretas.
erradas = '' #Variavel com as letras erradas.
sorteio = ''
contadore = 0
letras = ''
texto = ''
n = ''
acerto  = False
            
def escolhe():

    global tamanhopalavra
    global letras
    global texto
    global sorteio

    tamanhopalavra = [] #Lista para o usuario identicar o tamanho da palavra  
    sorteio = ''
    letras = ''
    texto = ''
    acerto  = False

    site = urllib.request.urlopen('https://www.ime.usp.br/~pf/dicios/br') #Aqui eu estou pegando as palavras no site
    texto = site.read().decode('iso8859').lower().split() #Transformando as palavras pegas , em lista e deixando todas em minusculo.
    sorteio = random.choice(texto) #Sorteio da palavras para o jogo.

    if len(sorteio) < 5: #Verificando se a palavra sorteada for menor que 5 então vou sortear dnv.
        while len(sorteio) < 5:
            sorteio = random.choice(texto)

    sorteio.split() #Transformando a palavra em lista.

    for k in range(0,len(sorteio)):
        tamanhopalavra.append('-') #Adiciono '-' para cada caracter da palavra

    chute(letras) #Chamando função para jogar
    
def desenha():
    if contadore == 0:    
       print('''
  +-----+
  |     |
        |
        |
        |
        |
        |
=============
  ''')
    if contadore == 1:
       print ('''
  +-----+
  |     |
  O     |
        |
        |
        |
        |
=============''')
    if contadore == 2:
       print('''
  +-----+
  |     |
  O     |
  |     |
        |
        |
=============
''')
    if contadore == 3:
       print('''
  +-----+
  |     |
  O     |
  |     |
  |     |
        |
        |
=============
''')
    if contadore == 4:
       print ('''
  +-----+
  |     |
  O     |
  |\    |
  |     |
        |
        |
=============
''')
    if contadore == 5:
       print('''
  +-----+
  |     |
  O     |
 /|\    |
  |     |
        |
        |
=============
''')
    if contadore == 6:
       print('''
  +-----+
  |     |
  O     |
 /|\    |
  |     |
   \    |
        |
=============
''')
    if contadore == 7:
       print('''
  +-----+
  |     |
  O     |
 /|\    |
  |     |
 / \    |
        |
=============
''')
   
######################################################################
def chute(letras):
    global n
    global sorteio
    global certas
    global erradas
    global contadore

    acerto = False
    contadore = 0
    erradas = ''
    certas = ''

    num= ['0','1','2','3','4','5','6','7','8','9']
    carace= ['!','@','#','$','%','&','*','(',')','-','_','=','+','{','}','[',']','^','~','.',',','/','?','|','¬','',' ']

    while acerto ==  False:
        print (tamanhopalavra)
        desenha()
        n = str(input('\nEntre com a letra: ')) #Entrada do user
        
        t = False
        
        while t == False: #Teste de erro
           if n in num:
              n=str(input('Numeros são invalidos.\nEntre com a letra novamente: '))
           
           elif n in carace:
              n=str(input('Carácter especias são invalido.\nEntre com a letra novamente:: '))

           elif n in letras:
              n=str(input('Você já chutou essa letra.\nEntre com a letra novamente: '))

           else:
              t = True   
####Mostrando as variaves com as letras acertadas e erradas#####
        print ('Erradas:%s'%erradas)
        print ('Certas :%s'%certas)
        
        
        if n in sorteio: #Concatenação das variaveis certas
            certas = certas + n + ' '
        else:#Concatenação das variaves erradas
            erradas = erradas + n + ' '
            contadore += 1

        for k in range(0,len(sorteio)): #Verificando se o usuario acertou a letra se acertou substitui a posição '-' pela letra
            if n == sorteio[k]:
                tamanhopalavra[k] = n
                
        ganhou() #Chamando função pra verificar se ganhou
        letras = certas + erradas  #Concatenando erradas + certas para verificação abaixo   

def ganhou():
    global acerto
    global tamanhopalavra
    global contadore       

    if contadore == 7: #Verificando se o usuario ultrapassou o limite de erros
       print('Você perdeu !')
       jogar_novamente() #Perguntando se quer jogar dnv
       quit()

    for k in range (0,len(tamanhopalavra)): #Verificando se tem algum '-' na lista se tiver, retorna pra ele inserir novas letras 
        if tamanhopalavra[k] == '-':
           return

    if '-' not in tamanhopalavra: #Verificando se tem algum '-' na lista se não tiver o usuario ganhou
       acerto = True
       print ('\nVocê ganhou !!!\n')
       jogar_novamente()

def jogar_novamente(): #Função para perguntar se quer jogar dnv

    t = False
    while t == False:
          jgn = str(input('Você deseja jogar novamente ? (S/N): '))

          if jgn == 's' or jgn == 'S' or jgn == 'SIM' or jgn == 'sim':                   
             t = True
             escolhe() #Chamando função
                
          if jgn == 'n' or jgn == 'N' or jgn == 'NAO' or jgn == 'NÃO' or jgn == 'Não' or jgn == 'Não':
             t = True
             quit()
             
          if jgn != 's' or jgn != 'S' or jgn != 'SIM' or jgn != 'sim' or jgn != 'n' or jgn != 'N' or jgn != 'NAO' or jgn != 'NÃO' or jgn != 'Não' or jgn != 'Não':
             jgn = str(input('Opção invalida.\nVocê deseja jogar novamente ?(S/N): '))
             t = False

escolhe()
