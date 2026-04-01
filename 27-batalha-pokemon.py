import random

import os

os.system ("cls")

print("Sistema - Batalha Pokémon ⚡")

print ("=" * 40)

nome_jogador = input("Digite seu nome: ")

print ("=" * 40)

print(f"Seja bem-vindo, {nome_jogador}!\n")
print("Escolha seu pokémon:\n")
print("1 - Charmander 🔥")
print("2 - Squirtle 💧")
print("3 - Bulbasaur 🌱")

pokemon_escolhido = int(input("\nEscolha um número: "))
pokemon_inimigo = random.randint(1,3)

print ("=" * 40)

if pokemon_escolhido ==1:
    print("Você Escolheu: Charmander")

elif pokemon_escolhido ==2:
    print("Você Escolheu: Squirtle")

elif pokemon_escolhido ==3:
    print("Você Escolheu: Bulbasaur")

else:
    print("Número Inválido")


if pokemon_inimigo == 1:
    print("inimigo Escolheu: Charmander") 

elif pokemon_inimigo ==2:
    print("Inimigo Escolheu: Squirtle")

elif pokemon_inimigo ==3:
    print("Inimigo Escolheu: Bulbasaur")

else:
    print("Número Inválido")


print ("=" * 40)

input("Pressione <enter> para iniciar a batalha...")


if pokemon_escolhido ==1 and pokemon_inimigo ==1:
    print("Os dois usuários escolheram Charmander 🔥")
    print("Empate!")

elif pokemon_escolhido ==1 and pokemon_inimigo ==2:
    print("💧 Squirtle tem vantagem contra 🔥 Charmander")
    print("Inimigo venceu!")

elif pokemon_escolhido ==1 and pokemon_escolhido ==3:
    print("🔥 Charmander tem vantagem contra 🌱 Bulbasaur")
    print("Você venceu!")


elif pokemon_escolhido ==2 and pokemon_inimigo ==1:
    print("💧 Squirtle tem vantagem contra 🔥 Charmander")
    print("Você venceu!")

elif pokemon_escolhido ==2 and pokemon_inimigo ==2:
    print("Os dois usuários escolheram o Squirtle 💧")
    print("Empate!")

elif pokemon_escolhido ==2 and pokemon_inimigo ==3:
    print("🌱 Bulbasaur tem vantagem contra 💧 Squirtle ")
    print("Inimigo venceu!")


elif pokemon_escolhido ==3 and pokemon_inimigo ==1:
    print("🔥 Charmander tem vantagem contra 🌱 Bulbasaur")
    print("Inimigo venceu!")

elif pokemon_escolhido ==3 and pokemon_inimigo ==2:
    print("🌱 Bulbasaur tem vantagem contra 💧 Squirtle")
    print("Você venceu!")

elif pokemon_escolhido ==3 and pokemon_inimigo ==3:
    print("Os dois usuários escolheram o Bulbasaur 🌱")
    print("Empate!")

else:
    print("Batalha encerrada!")

print ("=" * 40)