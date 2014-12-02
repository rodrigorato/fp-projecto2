#variaveis de teste
#apaga isto depois!!!!!
t1 = [[1, 2, 4, 8], \
      [16, 32, 64, 128], \
      [256, 512, 1024, 2048], \
      [4096, 8192, 16384, 32768], \
      0]  

t2 = [[2, 2, 0, 0], \
      [2, 0, 2, 0], \
      [2, 0, 0, 2], \
      [0, 0, 2, 2], \
      0]

t3 = [[4, 4, 2, 2], \
      [4, 4, 4, 4], \
      [2, 0, 0, 2], \
      [0, 0, 2, 2], \
      0]




#Inicio
jogadas_validas = ('N', 'S', 'W', 'E')

#Construtor
#cria_coordenada: int x int -> coordenada
#em que int e um inteiro entre 1 e 4
def cria_coordenada(x, y):
    if (isinstance(x, int) and x in (1, 2, 3, 4)) and \
       (isinstance(y, int) and y in (1, 2, 3, 4)):
        return (x, y) 
    else:
        raise ValueError("cria_coordenada: argumentos invalidos")

#Selectores
#coordenada_linha: coordenada -> inteiro
def coordenada_linha(coordenada):
    return coordenada[0]

#coordenada_coluna: coordenada -> inteiro
def coordenada_coluna(coordenada):
    return coordenada[1]

#Reconhecedores
#e_coordenada: universal -> logico
def e_coordenada(arg):
    return (isinstance(arg, tuple) and len(arg) == 2)  and \
           (isinstance(arg[0], int) and arg[0] in (1, 2, 3, 4)) and \
           (isinstance(arg[1], int) and arg[1] in (1, 2, 3, 4))  

#coordenadas_iguais: coordenada x coordenada -> logico
def coordenadas_iguais(c1, c2):
    return coordenada_linha(c1) == coordenada_linha(c2) and \
           coordenada_coluna(c1) == coordenada_coluna(c2)


#TAD Tabuleiro

#Construtor
def cria_tabuleiro():
    return [[0, 0, 0, 0], \
            [0, 0, 0, 0], \
            [0, 0, 0, 0], \
            [0, 0, 0, 0], \
            0]              #resultado

#Selectores
def tabuleiro_posicao(tab, coord):
    if not e_coordenada(coord):
        raise ValueError("tabuleiro_posicao: argumentos invalidos")
    else:
        return tab[coordenada_linha(coord) - 1][coordenada_coluna(coord) - 1]

def tabuleiro_pontuacao(tab):
    return tab[4]

def tabuleiro_posicoes_vazias(tab):
    lista_coordenadas_vazias = []
    for linha in range(1, 5):
        for coluna in range(1, 5):
            coord = cria_coordenada(linha, coluna)
            if tabuleiro_posicao(tab, coord) == 0:
                lista_coordenadas_vazias = lista_coordenadas_vazias + [coord]
    return lista_coordenadas_vazias

def tabuleiro_preenche_posicao(tab, coord, num):
    if not e_coordenada(coord):
        raise ValueError("tabuleiro_preenche_posicao: argumentos invalidos")
    else:
        tab[coordenada_linha(coord) - 1][coordenada_coluna(coord) - 1] = num
        return tab

def tabuleiro_actualiza_pontuacao(tab, numero):
    if not pontuacao_valida(numero):
        raise ValueError("tabuleiro_actualiza_pontuacao: argumentos invalidos")
    else:
        tab[4] = tabuleiro_pontuacao(tab) + numero
        return tab

#junta aos seletores
def pontuacao_valida(arg):
    return isinstance(arg, int) and arg >= 0 and arg % 4 == 0
# junta!!




def tabuleiro_reduz(tab, jogada):
    def linha_para_lista_tabuleiro(tab, linha):
        #le os valores de dada linha de um tabuleiro e devolve-os
        #como uma lista
        lista = []
        for coluna in range(1, 5):
            lista = lista + [tabuleiro_posicao(tab, cria_coordenada(linha, coluna))]
        return lista
    
    def coluna_para_lista_tabuleiro(tab, coluna):
        #le os valores de dada coluna de um tabuleiro e devolve-os
        #como uma lista        
        lista = []
        for linha in range(1, 5):
            lista = lista + [tabuleiro_posicao(tab, cria_coordenada(linha, coluna))]
        return lista    
    
    def escreve_linha_tabuleiro(tab, linha, lista):
        #recebe um tabuleiro, um inteiro que corresponde a uma linha e uma lista
        #escreve a lista nessa linha do tabuleiro
        for coluna in range(len(lista)):
            tabuleiro_preenche_posicao(tab, cria_coordenada(linha, coluna + 1), lista[coluna])
    
    def escreve_coluna_tabuleiro(tab, coluna, lista):
        #recebe um tabuleiro, um inteiro que corresponde a uma coluna e uma lista
        #escreve a lista nessa coluna do tabuleiro
        for linha in range(len(lista)):
            tabuleiro_preenche_posicao(tab, cria_coordenada(linha + 1, coluna), lista[linha])        
    
    def move_lista_dir(lista):
        #Movimento a direita:
        #recebe uma lista correspondente a uma linha ou coluna de um tabuleiro
        #e faz a sua reducao. aplicada linha a linha ou coluna a coluna para
        #reduzir a totalidade do tabuleiro
        def aux (lista,lista_aux):
            if lista==[]:
                return lista_aux
            elif lista[0]==0:
                return aux(lista[1:],[0]+lista_aux)
            else:
                return aux(lista[1:],lista_aux+[lista[0]])
        return aux (lista,[])
            
    def move_lista_esq(lista):
        #Movimento a esquerda:
        #recebe uma lista correspondente a uma linha ou coluna de um tabuleiro
        #e faz a sua reducao. aplicada linha a linha ou coluna a coluna para
        #reduzir a totalidade do tabuleiro        
        def aux (lista,lista_aux):
            if lista==[]:
                return lista_aux
            elif lista[-1]==0:
                return aux(lista[:-1], lista_aux+[0])
            else:
                return aux(lista[:-1],[lista[-1]]+lista_aux)
        return aux (lista,[])
    
    def soma_lista_aux(lista, tab):
        #Soma os elementos adjacentes de uma lista que representa
        #ou uma linha ou uma coluna de um tabuleiro.
        for elemento in range(len(lista) - 1):
            if lista[elemento] == lista[elemento + 1]:
                tabuleiro_actualiza_pontuacao(tab, lista[elemento]*2)
                lista[elemento] = lista[elemento] * 2
                lista[elemento + 1] = 0
        return lista
     
    def reduz_linhas_aux(tab, jogada):
        if jogada == 'W':
            for linha in range(1, 5):
                lista = linha_para_lista_tabuleiro(tab, linha)
                lista = move_lista_esq(soma_lista_aux(move_lista_esq(lista), tab))
                escreve_linha_tabuleiro(tab, linha, lista)
        else:
            for linha in range(1, 5):
                lista = linha_para_lista_tabuleiro(tab, linha)
                lista = move_lista_dir(soma_lista_aux(move_lista_dir(lista), tab))
                escreve_linha_tabuleiro(tab, linha, lista)
    
    def reduz_colunas_aux(tab, jogada):
        if jogada == 'N':
            for coluna in range(1, 5):
                lista = coluna_para_lista_tabuleiro(tab, coluna)
                lista = move_lista_esq(soma_lista_aux(move_lista_esq(lista), tab))
                escreve_coluna_tabuleiro(tab, coluna, lista)
        else:
            for coluna in range(1, 5):
                lista = coluna_para_lista_tabuleiro(tab, coluna)
                lista = move_lista_dir(soma_lista_aux(move_lista_dir(lista), tab))
                escreve_coluna_tabuleiro(tab, coluna, lista)        
   
    if not jogada in jogadas_validas:
        raise ValueError("tabuleiro_reduz: argumentos invalidos")
    elif jogada == 'N' or jogada == 'S':
        reduz_colunas_aux(tab, jogada)
    else:   #jogada == 'E' or jogada == 'W'
        reduz_linhas_aux(tab, jogada)
    return tab



def e_tabuleiro(arg):
    #nao verifica se os elementos sao potencias de 2
    return isinstance(arg, list) and len(arg) == 5 and \
           isinstance(arg[0], list) and len(arg[0]) == 4 and \
           isinstance(arg[1], list) and len(arg[1]) == 4 and \
           isinstance(arg[2], list) and len(arg[2]) == 4 and \
           isinstance(arg[3], list) and len(arg[3]) == 4 and \
           pontuacao_valida(arg[4])

def tabuleiro_terminado(tab):
    return tabuleiro_posicoes_vazias(tab) == [] and \
           not existem_movimentos(tab)

#nao esta no enunciado
def existem_movimentos(tab):
    for linha in range(1, 5):
        for coluna in range(1, 4):
            if tabuleiro_posicao(tab, cria_coordenada(linha, coluna)) == \
               tabuleiro_posicao(tab, cria_coordenada(linha, coluna + 1)):
                return True
    
    for coluna in range(1, 5):
        for linha in range(1, 4):
            if tabuleiro_posicao(tab, cria_coordenada(linha, coluna)) == \
                tabuleiro_posicao(tab, cria_coordenada(linha + 1, coluna)):
                return True
            
    return False
#documentar /\

def tabuleiros_iguais(t1, t2):
    if tabuleiro_pontuacao(t1) != tabuleiro_pontuacao(t2):
        return False
        
    for linha in range(1, 5):
        for coluna in range(1, 5):
            if tabuleiro_posicao(t1, cria_coordenada(linha, coluna)) != \
               tabuleiro_posicao(t2, cria_coordenada(linha, coluna)):
                return False
    return True

def escreve_tabuleiro(tabuleiro):
    if not e_tabuleiro(tabuleiro):  #verifica validade do tabuleiro
        raise ValueError("escreve_tabuleiro: argumentos invalidos")
    
    linha_a_escrever = ""
    for linha in range(1,5):
        for coluna in range(1, 5):
            linha_a_escrever = linha_a_escrever + "[ " + \
                str(tabuleiro_posicao(tabuleiro, cria_coordenada(linha, coluna))) + " ] "
        print(linha_a_escrever)
        linha_a_escrever = ""
    
    print("Pontuacao: " + str(tabuleiro_pontuacao(tabuleiro))) 

def pede_jogada():
    