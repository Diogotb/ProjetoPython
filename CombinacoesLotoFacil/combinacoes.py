# Um programa Python para imprimir todas as
# combinações de determinado comprimento
from itertools import combinations

# Obtem todas as combinações de [1, 2, 3] 
# e tamanho 2
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
comb = combinations(numeros, 15)

# imprime todas as combinações e escreve no arquivo
f = open("combinacoes.txt", "w")
for i in list(comb):
    if sum(i)<205 and sum(i)>185:
        if i[0]+4!=i[4] and i[1]+4!=i[5] and i[2]+4!=i[6] and i[3]+4!=i[7] and i[4]+4!=i[8] and i[5]+4!=i[9] and i[6]+4!=i[10] and i[7]+4!=i[11] and i[8]+4!=i[12] and i[9]+4!=i[13] and i[10]+4!=i[14]:
            impares = [num for num in i if num % 2 == 1]
            nimpares = len(impares)
            if nimpares<9 and nimpares>5:
                if i[0]<5 and i[1]<6 and i[2]<7 and i[3]<10 and i[4]<11 and i[5]<12:
                    if i[14]>20 and i[13]>19 and i[12]>18 and i[11]>15 and i[10]>14 and i[9]>13:
                        if i[6]>9 and i[7]>10 and i[8]>11 and i[6]<16 and i[7]<17 and i[8]<18:
                            # print (i)
                            f.write(str(i))
                            f.write('\n')
