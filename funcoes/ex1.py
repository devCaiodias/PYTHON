def duplicar(n):
    return n*2

def triplica(n):
    return n*3

def quadriplica(n):
    return n*4

duplica = duplicar(2)
triplicaa = triplica(2)
quadriplicaa = quadriplica(2)

# print(duplica)
# print(triplicaa)
# print(quadriplicaa)

def dtq_calculos(n):
    def numero(n1):
        return n * n1
    return numero

dtq_resultado = dtq_calculos(2)

for numero in [2, 3, 4]:
    print(dtq_resultado(numero))
