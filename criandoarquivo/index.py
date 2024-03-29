import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Users\\caiod\\pyhard\\criandoarquivo\\'
caminho_arquivo += 'arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

def escrever_com_quebra_de_linha(msg):
    arquivo.write(f'{msg} \n')

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     escrever_com_quebra_de_linha('Caio lindo')
#     escrever_com_quebra_de_linha('papo')
#     arquivo.writelines(
#         ('Carro \n', 'Mota \n',)
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
    
#     print('-'*10)
    
#     print('Lendo')
#     arquivo.seek(0,0)
#     print(arquivo.readline().strip())
#     print(arquivo.readline())
    
#     print('-'*10)
       
#     print('READLINES')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
    
# print('-'*10)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    escrever_com_quebra_de_linha('Caio lindo')
    escrever_com_quebra_de_linha('papo')
    arquivo.writelines(
        ('Carro \n', 'Mota \n',)
    )
    
# os.unlink(caminho_arquivo)
# os.rename(caminho_arquivo, 'arquivo-2.txt')