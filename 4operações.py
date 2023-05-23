op = 0
while op != 6:
    n1 = int(input('digite um numero: '))
    n2 = int(input('digite outro numero: '))
    while True:
        op = int(input(
            'Escolha uma opção:\n'
            '1. soma \n'
            '2. subtração \n'
            '3. multiplicação \n'
            '4. divisão \n'
            '5. novo numero \n'
            '6. sair \n'
        ))
        if op == 1:
            print("A soma dos dois numeros é:",n1+n2)
        if op == 2:
            print("A subtração dos dois numeros é:",n1-n2)
        if op == 3:
            print("A multiplicação dos dois numeros é:",n1*n2)
        if op == 4:
            print("A divisão dos dois numeros é:",n1/n2)
        if op == 5:
            break
        if op == 6:
            print('programa encerrado')
            break