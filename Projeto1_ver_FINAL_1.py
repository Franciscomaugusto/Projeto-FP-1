def eh_tabuleiro(tab):
    """Esta funcao recebe um argumento de qualquer tipo, verifica se o argumento\
 que lhe e dado e um tabuleiro, e devolve True caso o seja"""
    if not isinstance(tab, tuple) or len(tab) != 3:
        return False
    for i_1 in range(0, 3):
        if not isinstance(tab[i_1], tuple) or len(tab[i_1]) != 3:
            return False
        for i_2 in range(0, 3):
            if not (tab[i_1][i_2] in range(-1, 2)):
                return False
    return True

def eh_posicao(val):
    """Esta funcao verifica se o argumento inserido e um inteiro do intervalo [1,9]"""
    if isinstance(val, int) and not isinstance(val, bool) and val in range(1, 10):  # Verifica se e efetivamente um inteiro e nao um boolian
            return True
    return False


def obter_coluna(tab, col):
    if eh_tabuleiro(tab) and col in range(1, 4):
        res = ()
        for v in range(0, 3):
            res = res + (tab[v][col-1],)
        return res
    raise ValueError('obter_coluna: algum dos argumentos e invalido')


def obter_linha(tab, line):
    if eh_tabuleiro(tab) and line in range(1, 4):
        res = ()
        for v in range(0, 3):
            res = res + (tab[line-1][v],)
        return res
    raise ValueError('obter_linha: algum dos argumentos e invalido')


def obter_ponto(tab,lin,col): #funcao auxiliar que obtem pontos especificos
    return tab[lin-1][col-1]
    

def obter_diagonal(tab, diag):
    if eh_tabuleiro(tab) and diag in [1,2]:
        if diag == 1:
            res = (obter_ponto(tab,1,1),obter_ponto(tab,2,2),obter_ponto(tab,3,3) )
        if diag == 2:
            res = (obter_ponto(tab,3,1),obter_ponto(tab,2,2),obter_ponto(tab,1,3) )
        return res
    raise ValueError('obter_diagonal: algum dos argumentos e invalido')


def codifica(linha):  # funcao auxiliar para facilitar a escrita da funcao tabuleiro_str
    nova_linha = ()
    for c in linha:
        if c == 1:
            nova_linha = nova_linha + (' X ',)
        if c == -1:
            nova_linha = nova_linha + (' O ',)
        if c == 0:
            nova_linha = nova_linha + ('   ',)
    return nova_linha


def tabuleiro_str(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')    
    linha_1 = codifica(obter_linha(tab, 1))  # Invoquei a funcao aux para trocar os numeros pelos respetivos simbolos
    linha_2 = codifica(obter_linha(tab, 2))  # Repeti para todas as linhas
    linha_3 = codifica(obter_linha(tab, 3))
    res = str(linha_1[0]) + '|' + str(linha_1[1]) + '|' + str(linha_1[2])+'\n' + '----------- \n' + str(linha_2[0]) + '|' + str(linha_2[1]) + '|' + str(linha_2[2])+'\n' + '----------- '+'\n' + str(linha_3[0]) + '|' + str(linha_3[1]) + '|' + str(linha_3[2])
    return res

def eh_posicao_livre(tab, val):
    if not(eh_tabuleiro(tab)) or not eh_posicao(val):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    if val in range(1, 4) and tab[0][val-1] == 0:
        return True
    if val in range(4, 7) and tab[1][val-4] == 0:
        return True
    if val in range(7, 10) and tab[2][val-7] == 0:
        return True
    else:
        return False


def obter_posicoes_livres(tab):
    if eh_tabuleiro(tab):
        res = ()
        for i in range(1, 10):
            if eh_posicao_livre(tab, i):
                res = res + (i, )
        return res
    raise ValueError('obter_posicoes_livres: o argumento e invalido')


def junta_col(tab):
    return ((obter_coluna(tab,1),obter_coluna(tab,2),obter_coluna(tab,3)))
    

def ganha_linhas(tab):
    for x in range(0,3):
        tup = tab[x]
        if tup[0] + tup[1] + tup[2] == -3:
            return -1
        if tup[0] + tup[1] + tup[2] == 3:
            return 1
    return 0
 
        
def ganha_diag(tab):
        if tab[0]==1 and tab[1]==1 and tab[2]==1:
            return 1
        if  tab[0]==-1 and tab[1]==-1 and tab[2]==-1:
            return -1
        else:
            return 0
        
 
def jogador_ganhador(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    if ganha_linhas(tab) != 0:
        return ganha_linhas(tab)
    test_col = junta_col(tab)
    if ganha_linhas(test_col) != 0:
        return ganha_linhas(test_col)
    diag_1 = obter_diagonal(tab,1)
    if ganha_diag(diag_1) !=0:
        return ganha_diag(diag_1)
    diag_2 = obter_diagonal(tab,2)
    return ganha_diag(diag_2)
   
    
def editar_linha(linha,pos, num):
    i = 0
    novo_tup = ()
    while i<3:
        if i == pos:
            novo_tup = novo_tup + (num,)
        if i!= pos:
            novo_tup = novo_tup + (linha[i],)
        i=i+1
    return novo_tup


def marcar_posicao(tab, num, pos):
    if num in [-1,1] and eh_posicao_livre(tab,pos):
            if pos in range(1,4):
                pos = pos -1
                novo_tup = editar_linha(obter_linha(tab,1), pos, num)
                preserva_1 = obter_linha(tab,2)
                preserva_2 = obter_linha(tab,3)                
                tab =(novo_tup, preserva_1, preserva_2)
            if pos in range(4,7):
                pos = pos -4
                novo_tup = editar_linha(obter_linha(tab,2), pos, num)
                preserva_1 = obter_linha(tab,1)
                preserva_2 = obter_linha(tab,3)                
                tab = (preserva_1, novo_tup, preserva_2)                
            if pos in range (7,10):
                pos = pos - 7
                novo_tup = editar_linha(obter_linha(tab,3), pos, num)
                preserva_1 = obter_linha(tab,1)
                preserva_2 = obter_linha(tab,2)                   
                tab =(preserva_1, preserva_2, novo_tup)
            return tab
    raise ValueError('marcar_posicao: algum dos argumentos e invalido')


def escolher_posicao_manual(tab):
    pos = eval(input('Turno do jogador. escolha uma posicao livre: '))
    if not eh_posicao_livre(tab,pos):
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    return pos
 
 
def encontra_livre(serie):
    for index in range(0,3):
        if serie[index] == 0:
            return (index+1) 
    return False

def verifica_linhas(tab,num):
    offsets = [0,3,6]
    for index in range(1,4):
        linha = obter_linha(tab, index)
        if linha.count(num) == 2:
            livre = encontra_livre(linha)
            if not isinstance(livre,bool):
                return livre + offsets[index-1]   
    return False

def verifica_colunas(tab, num):
    variacoes = {1:1, 2:4, 3:7, 4:2, 5:5, 6:8, 7:3, 8:6, 9:9}
    novo_tab = junta_col(tab)
    valor= verifica_linhas(novo_tab, num)
    if isinstance(valor,bool):
        return False
    return variacoes[valor]
    
               
def verifica_diag(tab, num):
    diag1 = {1:1, 2:5, 3:9}
    diag = obter_diagonal(tab,1)
    if diag.count(num)==2:
        livre = encontra_livre(diag)
        if not isinstance(livre, bool):
            return diag1[livre]
    diag2 ={1:7, 2:5, 3:3}
    diag = obter_diagonal(tab,2)
    if diag.count(num)==2:
        livre = encontra_livre(diag)
        if not isinstance(livre, bool):
            return diag2[livre]
    return False
        
        
#Verificardor vitoria
def funcao_vitoria(tab, num):
    pos = verifica_linhas(tab,num)
    if isinstance(pos, bool):
        pos = verifica_colunas(tab, num)
        if isinstance(pos, bool):
            pos = verifica_diag(tab, num)
    return pos

def linha(pos):
    if pos not in range(1,10):
        raise ValueError('linha: o argumento e invalido')
    if pos in [1,2,3]:
        return 1
    if pos in [4,5,6]:
        return 2
    if pos in [7,8,9]:
        return 3


def coluna(pos):
    if pos not in range(1,10):
        raise ValueError('coluna: o argumento e invalido')
    if pos in [1,4,7]:
        return 1
    if pos in [2,5,8]:
        return 2
    if pos in [3,6,9]:
        return 3


def valor_posicao(tab, pos):
    l = linha(pos)
    c = coluna(pos)
    return tab[l-1][c-1]
    
    
def canto_oposto(tab,num):
    opostos = {1:9, 3:7, 7:3, 9:1}
    jogador = -1* num
    for canto in[1,3,7,9]:
        if valor_posicao(tab,canto) == jogador and eh_posicao_livre(tab,opostos[canto]):
            return opostos[canto]
    return False


def calcula_intersecao(tab, computador,pos_1, pos_2):

    def eh_bifurcacao(tab,linha,coluna, computador):
        l2 = obter_linha(tab, linha)
        c2 = obter_coluna(tab, coluna)
        jogador = -1* computador
        if l2.count(jogador) == 0 and c2.count(jogador) == 0:
            return True
        return False

    l1 = linha(pos_1)
    c1 = coluna(pos_2)
    if tab[l1-1][c1-1]==0 and eh_bifurcacao(tab,l1,c1,computador):
        return ((l1 -1)*3 + c1)
    return False



def bifurcacao(tab, computador):
    for index_1 in range(1,7):
        if valor_posicao(tab,index_1) == computador:
            for index_2 in range(index_1 +1, 10):
                if valor_posicao(tab,index_2) == computador:
                    interse = calcula_intersecao(tab, computador, index_1, index_2)
                    if not isinstance(interse, bool):
                        return interse
                    interse = calcula_intersecao(tab, computador, index_2, index_1)
                    if not isinstance(interse, bool):
                        return interse
                    interse = bifurca_diagonais(tab,computador, index_1, index_2)
                    if not isinstance(interse, bool):
                        return interse
                    interse = bifurca_diagonais(tab,computador, index_2, index_1)
                    if not isinstance(interse, bool):
                        return interse
    return False


def bifurca_diagonais(tab,computador, pos_1, pos_2):
    opostos_canto={1:9,3:7,7:3,9:1}
    jogador = -1*computador
    opostos_lateral = {2:8, 4:6, 6:4, 8:2}
    if pos_1 in [1,3,7,9] and pos_2 in [2,4,6,8] and eh_posicao_livre(tab,5) \
       and eh_posicao_livre(tab,opostos_canto[pos_1]):
        l_pos2 = linha(pos_2)
        c_pos2 = coluna(pos_2)
        l1 = obter_linha(tab, l_pos2)
        c1 = obter_coluna(tab, c_pos2)
        if pos_2 in [4,6]:
            if l1.count(jogador) == 0:
                return 5
            if c1.count(jogador) == 0:
                return opostos_canto[pos_1]
        if pos_2 in [2,8]:
            if c1.count(jogador) == 0:
                return opostos_canto[pos_1] 
            if l1.count(jogador) ==0:
                return 5
    return False


 
def aplica_criterio(tab, num, crit):
    jogador = -1 * num
    computador = num
    if crit == 1:
        return funcao_vitoria(tab, computador)
    if crit == 2:
        return funcao_vitoria(tab, jogador)
    if crit == 3:
        return bifurcacao(tab, computador) 
    if crit == 4:
        return bifurcacao(tab,jogador)
    if crit == 5:
        if eh_posicao_livre(tab,5):
            return 5
        return False
    if crit == 6:
        return canto_oposto(tab, num)
    if crit == 7:
        for x in [1,3,7,9]:
            if eh_posicao_livre(tab,x):
                return x
        return False
    if crit == 8:
        print('8')
        for x in [2,4,6,8]:
            if eh_posicao_livre(tab,x):
                return x
        return False
   
    
def escolher_posicao_auto(tab,num, modo):
    if eh_tabuleiro(tab) or  not num in [-1,1]:
        if modo == 'basico':
            for crit in [5,7,8]:    
                pos = aplica_criterio(tab, num, crit)
                if not isinstance(pos, bool):
                    return pos
        if modo == 'normal':
            for crit in [1,2,5,6,7,8]:    
                pos = aplica_criterio(tab, num, crit)
                if not isinstance(pos, bool):
                    return pos
        if modo == 'perfeito':
            for crit in [1,2,3,4,5,6,7,8]:
                pos = aplica_criterio(tab, num, crit)
                if not isinstance(pos, bool):
                    return pos
    raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    

def jogar(peca, modo):
    tab =((0,0,0),(0,0,0),(0,0,0))
    livres = obter_posicoes_livres(tab)
    codigo = {-1:'O', 1:'X'}
    if peca =='X':
        jogador = 1
        computador = -1
        while jogador_ganhador(tab) == 0 and livres !=(): 
            pos = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, jogador, pos)
            ecra =tabuleiro_str(tab)
            print(ecra)
            livres = obter_posicoes_livres(tab)
            if jogador_ganhador(tab) == 0 and livres!=():
                pos= escolher_posicao_auto(tab, computador, modo)
                print('Turno do computador (' + modo + '):')
                tab = marcar_posicao(tab, computador, pos) 
                ecra = tabuleiro_str(tab)
                print(ecra)
    if peca =='O':
        jogador = -1
        computador = 1
        while jogador_ganhador(tab) ==0 and livres !=(): 
            pos= escolher_posicao_auto(tab, computador, modo)
            print('Turno do computador (' + modo + '):')
            tab = marcar_posicao(tab, computador, pos) 
            ecra = tabuleiro_str(tab)
            print(ecra)
            livres = obter_posicoes_livres(tab)
            if jogador_ganhador(tab) == 0 and livres !=( ):
                pos = escolher_posicao_manual(tab)
                tab = marcar_posicao(tab,jogador, pos)
                ecra = tabuleiro_str(tab)
                print(ecra)
    if jogador_ganhador(tab)!=0:
        vencedor = codigo[jogador_ganhador(tab)]
        print('\'' + vencedor + '\'')
    elif livres ==():
        print('EMPATE')  

def jogo_do_galo(peca, modo):
    if peca in ['X','O'] and modo in ['basico', 'normal', 'perfeito']:
        print('Bem vindo ao JOGO DO GALO.\n O jogador comeca com \'' + peca + '\'.')
        jogar(peca, modo)