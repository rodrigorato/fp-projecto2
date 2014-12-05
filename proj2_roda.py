# Grupo 001 - Pedro Correia 81002 - Rodrigo Rato 81500

from random import random 

#TAD Coordenada

def cria_coordenada(x, y):
    """Construtor: recebe int x, int y em que x e y sao inteiros entre 1 e 4 e devolve o tipo coordenada"""
    if (isinstance(x, int) and x in (1, 2, 3, 4)) and \
       (isinstance(y, int) and y in (1, 2, 3, 4)):
        return (x, y) 
    else:
        raise ValueError("cria_coordenada: argumentos invalidos")


def coordenada_linha(coordenada):
    """Selector: recebe tipo coordenada e retorna inteiro correspondente a' linha"""
    return coordenada[0]


def coordenada_coluna(coordenada):
    """Selector: recebe tipo coordenada e retorna inteiro correspondente a' coluna"""
    return coordenada[1]


def e_coordenada(arg):
    """Reconhecedor: recebe um argumento e retorna valor logico True se for uma coordenada e False em caso contrario"""
    return (isinstance(arg, tuple) and len(arg) == 2)  and \
           (isinstance(arg[0], int) and arg[0] in (1, 2, 3, 4)) and \
           (isinstance(arg[1], int) and arg[1] in (1, 2, 3, 4))  


def coordenadas_iguais(c1, c2):
    """Reconhecedor: recebe duas coordenadas e devolve o valor logico True se forem iguais e False em caso contrario"""
    return coordenada_linha(c1) == coordenada_linha(c2) and \
           coordenada_coluna(c1) == coordenada_coluna(c2)


#TAD Tabuleiro

def cria_tabuleiro():
    """Construtor: nao recebe argumentos e retorna um elemento do tipo tabuleiro com todas as posicoes com o valor 0 e pontuacao 0"""
    return [[0, 0, 0, 0] , [0, 0, 0, 0] , [0, 0, 0, 0] , [0, 0, 0, 0] , 0]


def tabuleiro_posicao(tab, coord):
    """Selector: recebe um tabuleiro e uma coordenada e retorna o valor nessa coordenada"""
    if not e_coordenada(coord):
        raise ValueError("tabuleiro_posicao: argumentos invalidos")
    else:
        return tab[coordenada_linha(coord) - 1][coordenada_coluna(coord) - 1]


def tabuleiro_pontuacao(tab):
    """Selector: recebe um tabuleiro e retorna a pontuacao"""
    return tab[4]


def linha_para_lista_tabuleiro(tab, linha):
        """Selector: recebe um tabuleiro e um numero correspondente a uma linha e devolve todos os valores da linha como uma lista"""
        lista = []
        for coluna in range(1, 5):
            lista = lista + [tabuleiro_posicao(tab, cria_coordenada(linha, coluna))]
        return lista


def tabuleiro_posicoes_vazias(tab):
    """Selector: recebe um tabuleiro e devolve uma lista com as coordenadas onde existem elementos com o valor 0"""
    lista_coordenadas_vazias = []
    for linha in range(1, 5):
        for coluna in range(1, 5):
            coord = cria_coordenada(linha, coluna)
            if tabuleiro_posicao(tab, coord) == 0:
                lista_coordenadas_vazias = lista_coordenadas_vazias + [coord]
    return lista_coordenadas_vazias


def roda_tabuleiro(tab, num):
    """Modificador: recebe um tabuleiro e um numero n e gira o tabuleiro no sentido dos ponteiros do relogio n vezes"""
    new_tab=cria_tabuleiro()
    new_tab=tabuleiro_actualiza_pontuacao(new_tab, tabuleiro_pontuacao(tab))
    if num==0:
        return tab
    else:
        coluna=4
        for linhaTab in range(1, 5):
            lista=linha_para_lista_tabuleiro(tab, linhaTab)
            escreve_coluna_tabuleiro(new_tab, coluna, lista)
            coluna=coluna-1     
        return roda_tabuleiro(new_tab, num-1)


def pontuacao_valida(arg):
    """Reconhecedor: recebe um argumento e retorna o valor logico True se for uma pontuacao valida e False em caso contrario"""
    return isinstance(arg, int) and arg >= 0 and arg % 4 == 0


def escreve_linha_tabuleiro(tab, linha, lista):
    """Modificador: recebe um tabuleiro, um numero de uma linha e uma lista e substitui os elementos da linha pelos elementos da lista"""
    for coluna in range(len(lista)):
        tabuleiro_preenche_posicao(tab, cria_coordenada(linha, coluna + 1), lista[coluna])


def escreve_coluna_tabuleiro(tab, coluna, lista):
    """Modificador: recebe um tabuleiro, um numero de uma coluna e uma lista e substitui os elementos da coluna pelos elementos da lista"""
    for linha in range(len(lista)):
        tabuleiro_preenche_posicao(tab, cria_coordenada(linha + 1, coluna), lista[linha]) 


def tabuleiro_preenche_posicao(tab, coord, num):
    """Modificador: recebe um tabuleiro, uma coordenada e um numero e retorna o tabuleiro com o valor na coordenada igual ao numero"""
    if (not e_coordenada(coord)) or (not isinstance(num, int)):
        raise ValueError("tabuleiro_preenche_posicao: argumentos invalidos")
    else:
        tab[coordenada_linha(coord) - 1][coordenada_coluna(coord) - 1] = num
        return tab


def tabuleiro_actualiza_pontuacao(tab, numero):
    """Modificador: recebe um tabuleiro e um numero e retorna o tabuleiro com o numero acrescentado a' pontuacao"""
    if not pontuacao_valida(numero):
        raise ValueError("tabuleiro_actualiza_pontuacao: argumentos invalidos")
    else:
        tab[4] = tabuleiro_pontuacao(tab) + numero
        return tab


def tabuleiro_reduz(tab, jogada):
    """Modificador: recebe um tabuleiro e uma jogada e retorna um novo tabuleiro alterado de acordo com a jogada"""
   
    def move_lista_esq(lista):
            """Funcao que recebe uma lista e movimenta os elementos para a esquerda"""
            
            def aux (lista,lista_aux):
                if lista==[]:
                    return lista_aux
                elif lista[-1]==0:
                    return aux(lista[:-1], lista_aux+[0])
                else:
                    return aux(lista[:-1],[lista[-1]]+lista_aux)
                
            return aux (lista,[])
    
        
    def soma_lista_aux(lista,tab):
        """Funcao que recebe uma lista e um tabuleiro e devolve a lista com os elementos adjacentes somados e actualiza a pontuacao do tabuleiro"""
        for elemento in range(len(lista) - 1):
            if lista[elemento] == lista[elemento + 1]:
                tabuleiro_actualiza_pontuacao(tab, lista[elemento]*2)
                lista[elemento] = lista[elemento] * 2
                lista[elemento + 1] = 0
        return lista
       
    def aplica_jogada(tab):
        for linha in range(1, 5):
            lista = linha_para_lista_tabuleiro(tab, linha)
            lista = move_lista_esq(soma_lista_aux(move_lista_esq(lista), tab))
            escreve_linha_tabuleiro(tab, linha, lista)
        return tab   
   
   
    if jogada not in ('N', 'S', 'W', 'E'):
        raise ValueError("tabuleiro_reduz: argumentos invalidos")
    elif jogada == 'N' :
        tab=roda_tabuleiro(tab,3)
        tab=aplica_jogada(tab)
        tab=roda_tabuleiro(tab,1)
    elif jogada == 'S':
        tab=roda_tabuleiro(tab,1)
        tab=aplica_jogada(tab)
        tab=roda_tabuleiro(tab,3)
    elif jogada == 'E':
        tab=roda_tabuleiro(tab,2)
        tab=aplica_jogada(tab)
        tab=roda_tabuleiro(tab,2)
    else:                     #jogada == 'W'
        tab=aplica_jogada(tab)
    return tab


def e_tabuleiro(arg):
    """Reconhecedor: recebe um argumento e retorna o valor logico True se for um tabuleiro e False em caso contrario"""
    return isinstance(arg, list) and len(arg) == 5 and \
           isinstance(arg[0], list) and len(arg[0]) == 4 and \
           isinstance(arg[1], list) and len(arg[1]) == 4 and \
           isinstance(arg[2], list) and len(arg[2]) == 4 and \
           isinstance(arg[3], list) and len(arg[3]) == 4 and \
           pontuacao_valida(arg[4])


def tabuleiro_terminado(tab):
    """Reconhecedor: recebe um tabuleiro e retorna o valor logico True se o tabuleiro estiver cheio e nao existirem jogadas possiveis e False em caso contrario"""
        
    def existem_movimentos(tab):
        for jogada in ('N', 'S', 'E', 'W'):
            tab_depois_da_jogada = copia_tabuleiro(tab)
            tab_depois_da_jogada = tabuleiro_reduz(tab_depois_da_jogada, jogada)
            if not tabuleiros_iguais(tab, tab_depois_da_jogada):
                return True
        return False
 
    return tabuleiro_posicoes_vazias(tab) == [] and not existem_movimentos(tab)


def tabuleiros_iguais(t1, t2):
    """Teste: recebe dois tabuleiros e retorna True se forem iguais e False em caso contrario"""
    if tabuleiro_pontuacao(t1) != tabuleiro_pontuacao(t2):
        return False
    else:  
        for linha in range(1, 5):
            for coluna in range(1, 5):
                if tabuleiro_posicao(t1, cria_coordenada(linha, coluna)) != \
                   tabuleiro_posicao(t2, cria_coordenada(linha, coluna)):
                    return False
        return True


def escreve_tabuleiro(tabuleiro):
    """Funcao que recebe um tabuleiro e escreve no ecra a representacao externa"""
    if not e_tabuleiro(tabuleiro): 
        raise ValueError("escreve_tabuleiro: argumentos invalidos")
    
    linha_a_escrever = ""
    for linha in range(1,5):
        for coluna in range(1, 5):
            linha_a_escrever = linha_a_escrever + "[ " + \
                str(tabuleiro_posicao(tabuleiro, cria_coordenada(linha, coluna))) + " ] "
        print(linha_a_escrever)
        linha_a_escrever = ""
    
    print("Pontuacao:", tabuleiro_pontuacao(tabuleiro)) 


def copia_tabuleiro(tab1):
    """Funcao que recebe um tabuleiro e devolve uma copia desse tabuleiro."""
    novo_tab = cria_tabuleiro()
    tabuleiro_actualiza_pontuacao(novo_tab, tabuleiro_pontuacao(tab1))
    for coord in tabuleiro_posicoes_vazias(cria_tabuleiro()): #obtemos todas as coordenadas validas para qualquer tabuleiro
        tabuleiro_preenche_posicao(novo_tab, coord, \
                                   tabuleiro_posicao(tab1, coord))
    return novo_tab

#Jogo

def pede_jogada():
    """Funcao sem parametros que pergunta ao jogador a direcao (N,S,E,W)"""
    direcao=input("Introduza uma jogada (N, S, E, W): ")
    while direcao not in ('N', 'S', 'W', 'E'):
        print("Jogada invalida.")
        direcao=input("Introduza uma jogada (N, S, E, W): ")
    return direcao


def jogo_2048():
    """Funcao principal que permite jogar 2048"""
       
    def preenche_posicao_aleatoria(tab):
        if not len(tabuleiro_posicoes_vazias(tab)) == 0:    #Se ainda houver uma posicao vazia, preenchemo-la
            randCoord=tabuleiro_posicoes_vazias(tab)[int(random() * (len(tabuleiro_posicoes_vazias(tab)) - 1))] 
            if random() < 0.8:
                randNum=2
            else:
                randNum=4
            tabuleiro_preenche_posicao(tab,randCoord,randNum)    
        
    #comeca o jogo    
    tab=cria_tabuleiro()
    while not tabuleiro_terminado(tab):
            preenche_posicao_aleatoria(tab)     #geramos uma peca ao calhas e escrevemo-la no tabuleiro
            escreve_tabuleiro(tab)              #escrevemos a representacao externa do tabuleiro no ecra
            jogada=pede_jogada()                #pedimos a jogada ao utilizador e finalmente:
            tab = tabuleiro_reduz(tab, jogada)  #reduzimos o tabuleiro com a jogada dada
    #jogo acabou
            
    print("Jogo acabou, a sua pontuacao e de :", tabuleiro_pontuacao(tab))