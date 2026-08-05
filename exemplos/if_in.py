#Teste de conteúdo

print("\n------------------------------------------------------\n")

while True:
    
    num = input("Digite um número:\n")

    try:
        num = int(num)

        if num in range(0, 10):
            print(f"O número {num} está no range!")
        else:
            print(f"O número {num} não está no range.")

    except ValueError:
        print(f'"{num}" não é um número válido. Digite apenas inteiros!')

    input("\nPressione Enter para digitar outro número...")
    


    print("\n------------------------------------------------------\n")