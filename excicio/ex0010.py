# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

def add_tarefas(tarefa, lista=None):
    if lista is not None:
        lista = []
    lista.append(tarefa)
    return lista

tarefa = []
while True: 
    print('Comandos: listar, desfazer, refazer')
    tarefa_e_comendo = str(input('Dijite uma tarefa ou comando: '))
    
    print()
    
    if tarefa_e_comendo == 'listar':
        if tarefa == []:
            print('N tem nada na lista')
    elif tarefa_e_comendo == 'desfazer':
        tarefa_removida = tarefa.pop()
    elif tarefa_e_comendo == 'refazer':
        tarefa.append(tarefa_removida)
    else:
        tarefa.append(tarefa_e_comendo)
        
    print()
    print('TAREFAS:')
    for t in tarefa:
        print(t)
    print()
