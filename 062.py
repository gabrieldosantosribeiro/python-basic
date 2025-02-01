# Escreva um programa que crie duas listas com 5 números
# cada uma e exiba a soma dos elementos correspondentes das duas listas.
# Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1],
# o programa deve exibir [6, 6, 6, 6, 6].

l1 = [1,2,3,4,5]
l2 = [5,4,3,2,1]
l3 = []
for ele in range(0, 5):
    l3.append(l1[ele] + l2[ele])

print(l3)








