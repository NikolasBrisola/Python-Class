
'''

Dicionários

- Construtor: dict()
- Sintaxe: nome = {"chave" : valor}




aluno = {'nome' : 'João',
        'idade' : 23,
        'cidade' : 'São Paulo'}

#Imprimindo os dados do aluno

print(aluno)

#Acesso a um valor através da chave
print(f'\n\nNome: {aluno["nome"]}')

#Adicionar um novo elemento no dicinário
aluno['area'] = 'desenvolvedor'

print(aluno)

#Alterando um valor de uma chave

aluno['idade'] = 30
print(f'Nova idade: {aluno["idade"]}')








Exemplo 2

Principais métodos(mais comuns)

keys(): retorna uma "visão" de chaves do dicionário
values (): retorna uma "visão" de valores do dicionário
items(): retorna uma "visão" de item ( chave / valor ) do dicionário
get(): retorna um valor (de forma segura) 
retorna uma valor 

'''

carro = {
    "marca" : "Jeep",
    "modelo" : "Compass",
    "ano" : 2025
}

#iterando sobre as chaves do dicionário
for chave in carro.keys():
    print(chave)

#iterando sobre os valores do dicionário
for valor in carro.values():
    print(valor)

#iterando sobre os pares de chave-valor do dicionário
for chave, valor in carro.items():
    print(f'{chave} : {valor}') 


#print(carro["cor"]) -> Acesso ao dicionario com uma chave inexistente


#Acesso a um elemento do dicinário com método get() - evita 
print(f' cor: {carro.get})