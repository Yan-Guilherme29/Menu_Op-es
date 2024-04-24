import time

while True:
    print("-=" * 25)
    print("Bem vindo ao Programa!!")
    print("Escolha uma das Opções: ")
    print("\033[1;36m[0]\033[m - Sair")
    print("\033[1;36m[1]\033[m - Cálculos Matemáticos")
    print("\033[1;36m[2]\033[m - Simulador de Notas")
    print("\033[1;36m[3]\033[m - Tabuada")
    print("-=" * 25)


# O usuário irá digitar a opção que ele desejar

    opção = input("Digite o número da opção desejada: ")


# Nessa opção o programa será finalizado.

    if opção == "0":
        print("\033[1;36mSaindo do Programa...\033[m")
        time.sleep(1)
        print("\033[1;36m...\033[m")
        time.sleep(1)
        print("\033[1;36mFim !!!\033[m")
        break


# Nessa opção, o usuário irá dizer quantos números ele quer calcular, e quais os números.

    elif opção == "1":
        try:
            N1 = float(input("Digite o primeiro número do cálculo: "))

            N2 = float(input("Digite o segundo número do cálculo: "))

            print("-=" * 25)

            print(f"\033[1;32mSoma\033[m : {N1} + {N2} = \033[1;36m{N1 + N2}\033[m!")

            print(f"\033[1;32mSubtração\033[m : {N1} - {N2} = \033[1;36m{N1 - N2}\033[m!")

            print(f"\033[1;32mMultiplicação\033[m : {N1} * {N2} = \033[1;36m{N1 * N2}\033[m!")

            print(f"\033[1;32mDivisão\033[m : {N1} / {N2} = \033[1;36m{N1 / N2}\033[m!")

            print(f"\033[1;32mResto da Divisão\033[m : {N1} % {N2} = \033[1;36m{N1 % N2}\033[m!")

            print(f"\033[1;32mPotenciação\033[m : {N1} * {N2}  = \033[1;36m{N1 * N2}\033[m!")
            time.sleep(0.8)

        except ValueError:
            print("\033[1;31mPor favor, digite apenas números:\033[m ")


# Nessa opção o usuário irá dizer quantas notas ele quer calcular a média e quais são as notas.

    elif opção == "2":
        try:
            n_notas = int(input("Quantas notas você deseja calcular a média? "))
            soma_notas = 0

            # Aqui o programa irá pedir para o usuário digitar uma nota
            # conforme o número de notas em que o usuário pediu anteriormente.

            for c in range(n_notas):
                    notas = float(input("Digite sua Nota: "))
                    soma_notas += notas

            media = soma_notas / n_notas

            if media >= 6:
                print("...")
                time.sleep(1)
                print("Parabéns, você está Aprovado!")
                print(f"Média Final: \033[1;36m{media:.2f}\033[m")
                time.sleep(1.2)
            else:
                print("...")
                time.sleep(1)
                print("Que pena, você está Reprovado!")
                print(f"Média Final: \033[1;36m{media:.2f}\033[m")
                time.sleep(1.2)

        except ValueError:
            print("\033[1;31mPor favor, digite apenas números:\033[m ")



# Aqui o usuário irá digitar um número para que ele possa ver a tabuada do 1 ao 10 desse número desejado.

    elif opção == "3":
        try:
            numero = int(input("Digite um número para ver sua Tabuada: "))
            print("-=" * 25)
            for c in range(0, 11):
                calculo = numero * c
                print(f"{numero} x {c} = \033[1;36m{calculo}\033[m")

        except ValueError:
            print("\033[1;31mPor favor, digite apenas números:\033[m ")


# Aqui caso o usuário escolha uma opção que não esteja do 1 ao 3, o programa irá realizar o loop
# e irá retornar para o Menu de Opções.

    else:
        print("-=" * 25)
        print("\033[1;31mOpção inválida. Por favor, escolha uma opção válida.\033[m")
        time.sleep(0.5)

