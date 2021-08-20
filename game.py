#importar bibliotecas
import math
import random
import numpy as np

#criar variáveis
farm = []
farmy = []
i = []
j = []
modos = [0, 1, 2, 3, 4]
count = 0

#definir tamanho da fazendo e tipos dos quadrados
while count < 8:
    count2 = 0
    while count2 < 8:
        j = [random.choices(['~~', 'MM', 'oo'], [85, 10, 5], k=1)]
        i = i+j
        j = []
        count2 = count2 + 1 
    count = count + 1
    farm.append(i)
    print(i)
    i = []
count = 0
print("----------------------------------------------------------------------")

#desenhar a fazenda
farmy = np.array(farm)
for n in farmy:
    print ('  '.join(map(str, n)))

#while count < 8:
 #   x = []
 #   x = x + farm[count]
 #   for n in x:
 #       print (x[n])
  #  count = count + 1
#    t = input()


#
