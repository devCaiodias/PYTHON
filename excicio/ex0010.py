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
tarefa_refazer = []
while True: 
    print('Comandos: listar, desfazer, refazer')
    tarefa_e_comendo = str(input('Dijite uma tarefa ou comando: '))
    
    print()
    
    if tarefa_e_comendo == 'listar':
        if tarefa == []:
            print('N tem nada na lista')
            
    elif tarefa_e_comendo == 'desfazer':
        if not tarefa:
            print('Nenhuma tarefa para desfazer')
        else:
            tarefaa = tarefa.pop()
            tarefa_refazer.append(tarefaa)
        
    elif tarefa_e_comendo == 'refazer':
        if not tarefa_refazer:
            print('Nenhuma tarefa para refazer')
        else:
            tarefaa = tarefa_refazer.pop()
            tarefa.append(tarefaa)
    else:
        tarefa.append(tarefa_e_comendo)
        
    print()
    print('TAREFAS:')
    for t in tarefa:
        print(t)
    print()
    