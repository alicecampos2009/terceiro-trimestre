def rankJogador(pontos, derrotas):
    pontosFinais = pontos - (derrotas * 10)

    if pontosFinais < 0:
        return "Ops! Banido!"
    elif pontosFinais < 100:
        return "Parabéns! Bronze!"
    elif pontosFinais < 300:
        return "Parabéns! Prata!"
    elif pontosFinais < 600:
        return "Parabéns! Ouro!"
    else:
        return "Parabéns! Diamante!"
    
pontos = int(input("Digite seus pontos: "))
derrotas = int(input("Digite suas derrotas: "))

print(rankJogador(pontos, derrotas))