'''
8.	Sistema de notas com conceito
•	Peça a nota e exiba:
o	9 a 10 → "Excelente"
o	7 a 8.9 → "Bom"
o	5 a 6.9 → "Regular"
o	abaixo de 5 → "Insuficiente"

'''


print("\n--Sistema de notas com conceito--\n")

nota = float(input("Digite a nota: "))

if nota >= 9 and nota <= 10:
    print("Excelente")

elif nota >= 7:
    print("Bom")

elif nota >= 5:
    print("Regular")

else:
    print("Insuficiente")

print("\n--------------------------------\n")

