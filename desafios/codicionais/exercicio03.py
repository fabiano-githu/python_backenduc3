
'''
3.	Controle de desconto
•	Peça o valor da compra.
•	Se for maior que 100, mostre "Desconto aplicado!".
'''

'''
print("\n---Controle de desconto----\n")


valorcompra = input("Digite o valor da compra:\n")


try:

    valorcompra = float(valorcompra)

    if valorcompra>100:
        print("Desconto aplicado!")

except ValueError:
    print("Valor invalido! coloque ponto para dividir casas decimais")


print("\n---------------------------\n")
'''





while True:

    valorcompra = input("Digite o valor da compra: ")

    try:
        valorcompra = float(valorcompra)
        break  # Sai do loop quando o valor for válido

    except ValueError:
        print("Valor inválido! Tente novamente.")


   
if valorcompra > 100:
        print("Valor com desconto aplicado!")
else:
     print("Desconto não aplicado!")