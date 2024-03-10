frase = 'O Python é uma linguagem de programação multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'
    
i = 0
qtd_apareceu_mais_vez = 0
letra_que_apareceu_mais_vez = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vez < qtd_atual:
        qtd_apareceu_mais_vez = qtd_atual
        letra_que_apareceu_mais_vez = letra_atual
    
    i += 1
    
print(f'A letra que apareceu mais vezes foi "{letra_que_apareceu_mais_vez}" que apareceu, {qtd_apareceu_mais_vez}x')

# 71 AULA
