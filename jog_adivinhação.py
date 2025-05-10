import random
numero_secreto = random.randint (1,10)
tentativas = 0
contagem_tentativas = 0
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto")
while tentativas != numero_secreto: 
    numero = int(input("Digite um  número: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print("Prabéns, você acretou o número!")
        print(f"Você precisou de {contagem_tentativas} tentativas")
        break 
    elif numero < numero_secreto:
       print("O número secreto é maior.")
    else:
        print("O número secreto é menor") 
