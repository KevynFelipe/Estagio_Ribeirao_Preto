print("Contador da letra A iniciado")
contador_a = 0

frase = str(input("Escreva qualquer palavra ou frase que desejar: "))
for indice in frase:
    if 'a' == indice or 'A' == indice:
        contador_a += 1
print(f"Foram achadas {contador_a} letras A")
