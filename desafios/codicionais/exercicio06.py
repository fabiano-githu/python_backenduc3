'''
6.	Verificação de estoque
•	Peça quantidade disponível e quantidade pedida.
•	Se o pedido for maior que o estoque, exiba "Estoque insuficiente.".
•	Caso contrário, "Pedido confirmado.".

'''


print("\n--Verificação de estoque---\n")

quantidade = int(input("Digite a quantidade desponível: "))
pedido = int(input("Digite a quantidade pedida : "))
if pedido > quantidade:
    print("Estoque insuficiente!")
else:
    print("Pedido confirmado!")

print("\n---------------------------\n")
