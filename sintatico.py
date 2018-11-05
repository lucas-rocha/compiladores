import lexico
from utils import util_sin

def erro(a):
    global pilha

    #Indicando erro
    finais = 'Simbolos esperados: '
    s = pilha[-1]
    for terminal in util_sin.terminal:
        action = util_sin.t_analise[s][terminal]
        if not action == 'erro':
            finais+= terminal + '   '

    print(finais)


    # Tratando o erro
    while(True):
        s = pilha.pop(-1)
        aux = False
        for A in util_sin.nao_terminal:
            if not util_sin.t_analise[s][A] == '-1':
                aux = True
                break
        if aux:
            break

    while(True):
        s = pilha[-1]
        if a == False:
            return a
        action = util_sin.t_analise[s][a['token']]
        if action[0] == 's' or action[0] == 'r':
            return a
        elif a['token'] == '$':
            print('Erro sintatico invalida toda analise sintatica.')
            import sys
            sys.exit()
        a = lexico.analisador()


pilha = []
def main():
    global pilha

    a = lexico.analisador()

    pilha.append(0)

    while (True):
        if a == False:
            break
        s = pilha[-1]
        action = util_sin.t_analise[s][a['token']]

        if action[0] == 's':
            pilha.append(int(action[1:]))
            a = lexico.analisador()

        elif action[0] == 'r':
            regra = util_sin.gramatica[int(action[1:])-1]
            A = regra['A']
            B = regra['B']
            modulo_B = len(B.split())

            for i in range(modulo_B):
                pilha.pop(-1)

            t = pilha[-1]
            pilha.append(int(util_sin.t_analise[t][A]))

            print(A + ' -> ' + B)

        elif action == 'acc':
            break

        else:
            linha = lexico.get_l()
            print("Erro Sintatico(linha: " + str(linha) + ')')
            a = erro(a)

main()
