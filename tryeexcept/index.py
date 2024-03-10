"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

# numero_str = input('Vou dobrar o número que vc digitar: ')

# try:
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float:.2f}')

# except:
#     print('Isso n é um número')
    
# (Parte1) try e except para tratar exceções


# try:
#     a = 10
#     b = 0
#     # print(b[0])
#     print('LINHA 1'[1000])
#     c = a / b
# except ZeroDivisionError:
#     print('N pode dividir numero por zero')
# except NameError:
#     print('ERRO!') 
# except (TypeError, IndexError) as erro:
#     print('TypeError + IndexError')
#     print('MSG: ', erro)
#     print('Nome: ', erro.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO!')
    
# print('CONTINUAR')


# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIR O ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print('----------------------')
    print(e.__class__.__name__)
    print('----------------------')
    print(e)
    print('----------------------')
    print('N pode dividir numero com zero')
    
except IndexError as erro:
    print('IndexError')
    
except (NameError, ImportError):
    print('NameError, ImportError')
    
else:
    print('N deu erro')
    
finally:
    print('FECHEI O ARQUIVO')