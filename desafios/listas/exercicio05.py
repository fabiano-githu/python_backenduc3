
'''
Questão 5
Crie uma lista contendo:
[5, 10, 15, 20, 25]
Remova o número 15 utilizando o método adequado.
Exiba a lista final.

print("\n--------lista números-------\n")

listanum = [5, 10, 15, 20, 25]
listanum.remove(15, 10, 25)            xxxxx---DEU ERRO NÃO POSSO EXCLUIR VARIOS ITENS EM UM SÓ .REMOVE----XXXX
print(listanum)

print("\n---------------------------\n")

'''

print("\n--------lista números-------\n")

listanum = [5, 10, 15, 20, 25]
listanum.remove(15)
print(listanum)
listanum.remove(10)
print(listanum)
listanum.remove(20)
print(listanum)


print("\n---------------------------\n")