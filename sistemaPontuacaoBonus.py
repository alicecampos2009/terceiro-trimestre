def pontosTotais(pontos, tempo):
    if tempo < 30:
        pontos += 50
    elif tempo > 100:
        pontos -= 20

    if pontos > 200:
        return "Parabéns! Você atingiu um recorde!"
    else:
        return pontos
    
pontos = int(input("Digite a quantidade de pontos que você conseguiu: "))
tempo = int(input("Digite o tempo que você fez:"))

print(pontosTotais(pontos, tempo))