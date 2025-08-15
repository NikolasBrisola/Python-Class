


'''
Esceva um programa em Python que, para uma determinada qtde
de alunos, colete as notas de cada um e exiba um resumo da turma

O programa deve conter as seguintes funções:


1. coletar_notas() - usuário digita uma qtde de notas em uma única linha.
O prorama deve converter as notas para o formato númerico float e retorná-las em
uma lista

2. preencher_turma(qtde_alunos) - recebe a quantidade de alunos por parâmetro e,
para cada auno, deve chamar a função coletar_notas() para preeencher uma lista com
as notas dos alunos e retorná-las em uma lista (turma)

3. calcular_media(notas_aluno) - recebe uma lista de notas de um aluno e retorna 
a média aritmética das notas

4. resumo_turma() - percorre a lista de alunos (turma) e, para cada aluno,
exibir as notas e a média, formatando-a com duas casas decimais.


'''


def coletar_notas ():
    notas = input().split() #separa por espaços em branco
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    return notas


def preencher_turma(qtde_alunos):
    turma = []
    for i in range(qtde_alunos):
        print(f'{i+1}º aluno: ', end=" ")
        notas_aluno = coletar_notas()
        turma.append(notas_aluno)
    return turma
    

def calcular_media(notas_aluno):
    soma = 0
    for nota in notas_aluno:
        soma += nota
    return soma/len(notas_aluno)

def resumo_turma(turma):
    for notas_aluno in turma:
        media = calcular_media(notas_aluno)
        print(f'Notas: {notas_aluno} | Média {media:.2f}')

#Funão para testar o programa
def main():
    qtde_alunos = int(input('Quantidade de alunos: '))
    turma = preencher_turma(qtde_alunos)
    resumo_turma(turma) 

main()

    


