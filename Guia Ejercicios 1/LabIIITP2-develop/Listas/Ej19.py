lista=[[4,12,5,66],[14,6,25],[3,4,5,67,89,23,1],[78,56]]

print(lista)

for x in range(len(lista)):
    for y in range(len(lista[x])):
          if(lista[x][y] > 10):
                lista[x][y] = 0
print(lista)