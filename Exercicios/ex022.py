# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

nome = str(input("Qual o seu nome completo? "))
print("Seu nome com letras maiúsculas:", nome.upper())
print("Seu nome com letras minúsculas:", nome.lower())
print("Seu nome tem:", len(nome.replace(' ', '')), "letras.")
nome = nome.split()
print("Seu primeiro nome tem:", len(nome[0]), "letras.")
