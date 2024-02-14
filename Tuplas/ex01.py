''' O que é uma tupla?
lanche [misto, suco, pizza, pudim], tal que a posição é númererada por índices [0,1,2,3]
EX:
PRINT(LANCHE [2]) = PIZZA

PRINT(LANCHE [0:2]) = MISTO, SUCO

PRINT(LANCHE [1: ]) = SUCO, PIZZA, PUDIM

PRINT (LANCHE [-1]) = PUDIM

LEN É UMA REFERÊNCIA DE COMPRIMENTO 

A FUNÇÃO len (lanche) = 4 

for c in lanche: // aqui será criado a variável C e ela só aceita 1 comida, e nesse caso irá imprimir MISTO, depois volta e vai exibir o suco
    print(c) irá imprimir MISTO


AS TUPLAS SÃO IMUTÁVEIS, NÃO CONSIGO, POR EXEMPLO, MUDAR UMA TUPLA, NÃO CONSIGO COLOCAR A BOLO NO LUGAR DE PIZZA, EU TERIA QUE CRIAR OUTRA TUPLA
tupla em (), NA HORA DE REFERENCIAR []


for cont in range (0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}')

for comida in lanche:
    print (f'eu vou comerr {comida}')

print('comi pra caramba'!)

AMBOS DÃO O RESULTADO COMO

eu vou comer misto
eu vou comer suco
eu vou comer pizza
eu vou comer pudim
comi pra caramba



PARA DIZER A POSIÇÃO DO ELEMENTO
for cont in range (0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')


for pos, comida in enumerate (lanche):
    print (f'eu vou comerr {comida} na posição {pos}')

    
PARA POR O ELEMENTO EM ORDEM = ORGANIZADO
print(sorted (lanche)),
 vai printar em ordem alfabetica 
Misto, Pizza, Pudim, Suco


ORDEM IMPORTA
A = (2,5,4)
B= (5,8,1,2)
C = B + A
PRINT(C) = (5, 8, 1, 2, 2, 5, 4)
PRINT (LEN(C)) = 7
PRINT(C.COUNT(5)) = 2
PRINT(C.INDEX (8)) = 1, a posição que o 8 se encontra (5, 8, 1, 2, 2, 5, 4)
PRINT(C.INDEX (5)) = 0, a posição que o 5 se encontra (5, 8, 1, 2, 2, 5, 4) ele pega a primeira ocorrência
PRINT(C.INDEX (5,1)) = 1, a posição que o 5 se encontra (5, 8, 1, 2, 2, 5, 4), começa a contagem na posição 1 

pessoa = ('Gustavo, 39, 'M', 99.88)
print(pessoa)

não posso deletar um item da tupla, mas posso apagar a tupla inteira
del(pessoa)
'''
