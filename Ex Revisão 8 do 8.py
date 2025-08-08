
'''

Escreva um programa em Python que simule o cálculo de notas d um aluno em diferentes disciplinas.
O programa deve modular e utilizar as estruturas de controle e funções

1. Requisitos:
.Função calcular_media(notas)
 - deve receber uma Lisa de notas como parâmetro
 - deve ter uma estrutura de repetição (for ou while) para percorrer a lista
 - retorna a média das notas (com validações)
 
.Função verificar_aprovação(media, media_minima)
 - deve receber a média das notas e a média mínima para aprovação
 - deve usar condicionais para veificar o status do aluno
 - se a média for maior que a média mínima 7.0 , retornar a String "Aprovado"
 - se a media for maior ou igual a 5.0 e menor do que a média mínima retornar "Recuperação"
 - caso contrario, retorne a String "Reprovado. Tente novamente ano que vem"

.Função Principal main()
 - lista com as disciplinas
 - média mínima para apovação
 - estrutura de repetição para iterar sobre as disciplinas
 - para cada disciplina, o usuário deve inserir 3 notas
 - chamar a função calcular_media() para obter a média da disciplina
 - chamar a função verificar_aprovação() para obter o status do aluno 
 - imprimir a média e o status para cada disciplina
 -

'''


print("-----------------------")

def calcular_media(notas):
    '''
    Calcula a média de uma lista de notas
    - recebe por parâmetro uma lista de notas
    - retorna média das notas
    '''
    soma = 0

    #percorrer a lista de notas
    for nota in notas:
        soma = soma + nota

    if len(notas) > 0:
        return soma / len(notas)
    else:
        return 0
    
def verificar_aprovação(media, media_minima):
    '''
    Verifica o status de aprovação do aluno
    - recebe por parâmetro uma lista de notas
    - recebe a média mínima por parâmetro
    - retorna o status do aluno - aprovado, recuperação ou reprovado
    ''' 

    if media >= media_minima:
        return "Aprovado"
    elif media >= 5.0 and media < media_minima:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    '''
    Função principal do programa
    - lista com as discipinas
    - média mínima de aprovação

    '''
    #lista com as disciplinas

    disciplinas = ["Python", "Java", "Banco de Dados"]
    media_aprovacao = 7.0

    print(f'\n *--Sistema de Cálculo de notas --*\n')
    
    #percorre a lista de disciplinas
    for disciplina in disciplinas:
        print(f'Disciplina: {disciplina}')

        #lista com as notas
        notas = [] 

        #obter as notas por disciplina
        for i in range(3):
            nota = float(input(f'Digite a nota {i+1}'))
            notas.append(nota)

        #chamar as funções calcular_media() e verifica_aprovacao()
        media_final = calcular_media(notas)
        status = verificar_aprovação(media_final, media_aprovacao)

        #imprimir a média e o status
        print(f'Média em {disciplina}: {media_final:.2f}')
        print(f'Status: {status}')

#Programa Principal
main()





