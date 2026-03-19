def tipoMagia(fogo, agua):
    if fogo and agua:
        return "Você conseguiu fazer vapor!"
    elif fogo:
        return "Você conseguiu fazer fogo!"
    elif agua:
        return "Você conseguiu fazer água!"
    else: 
        return "Você não conseguiu fazer uma mágia..."
    
fogo = input("Você tem fogo? (S/N): ").upper() == "S"
agua = input("Você tem água? (S/N): ").upper() == "S"

print(tipoMagia(fogo, agua))