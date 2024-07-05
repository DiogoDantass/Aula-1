"""Escreva um programa que peça ao usuário para digitar uma frase e, em seguida,
conte quantas vogais (a, e, i, o, u) existem na frase utilizando um loop "for".""" 

frase = input("Digite uma frase")
total_a, total_e, total_i, total_o, total_u = 0,0,0,0,0

for letra in frase:

    if letra == "a":
        total_a += 1
    elif letra == "e"    