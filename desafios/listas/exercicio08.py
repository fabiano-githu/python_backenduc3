
'''
Questão 8
Crie uma lista com os números:
[50, 10, 80, 20, 40]
Ordene a lista em ordem crescente.
Exiba o resultado.

'''


print("\n------Ordem crescente e decrecente-----\n")

num2 = [50, 10, 80, 20, 40]

num2.sort() #crecente
print(f"{num2} a ordem é crescente!")

num2.sort(reverse=num2) #decrecente 
print(f"{num2} A ordem é decrescente!")

print("\n---------------------------\n")
