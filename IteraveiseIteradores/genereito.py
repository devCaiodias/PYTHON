# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maxmin=10):
    while True:
        yield n
        n += 1
        
        if n > maxmin:
            return 'ACABOU'
        

# gen = generator(maxmin=1000)
# for n in gen:
#     print(n)
    

# Yield from

def gen1():
    yield 1
    yield 2
    yield 3
    
def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6
    
gen = gen2()

for numero in gen:
    print(numero)