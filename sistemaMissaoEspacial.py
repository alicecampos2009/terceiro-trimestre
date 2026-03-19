def lancarFoguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Alerta de combustível insuficiente!"
    if clima != "bom":
        return "Alerta de clima desfavorável!"
    if not sistemaOk:
        return "Alerta de falha no sistema do foguete!"
    return "Lançamento autorizado"

combustivel = int(input("Digite a quantidade de combustível: "))
clima = input("Como está o clima? (bom/ruim): ").lower()
sistemaInput = input("Sistema operacional OK? (s/n): ").lower()
sistemaOk = sistemaInput == "s"

resultado = lancarFoguete(combustivel, clima, sistemaOk)
print("Resultado:", resultado) 