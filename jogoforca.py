import random

def forca():
    palavras = []
    for x in range(5):
        palavras.append(input("digite 10 palavras: "))
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ['_'] * len(palavra_secreta)
    tentativas_restantes = 6
    letras_digitadas = []

    print("\nJogo da Forca!\n")

    while True:
        print("\npalavra:", " ".join(letras_descobertas))
        print(f"restam {tentativas_restantes} tentativas")
        print("letras digitadas:", letras_digitadas)

        letra = input("digite uma letra: ").lower()

        if letra in letras_digitadas:
            print("você já digitou essa letra. tente novamente!")

        letras_digitadas.append(letra)

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas_restantes -= 1
            print("letra incorreta!")

        if '_' not in letras_descobertas:
            print("\nparabéns! você descobriu a palavra secreta:", palavra_secreta)
            break

        if tentativas_restantes == 0:
            print("\nvocê perdeu! A palavra secreta era:", palavra_secreta)
            break


forca()