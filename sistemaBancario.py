def saldoFinal(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    
    if saque > 1000:
        taxa = saque * 0.02
        saqueTotal = saque + taxa
    else:
        saqueTotal = saque

    saldoRestante = saldo - saqueTotal
    return saldoRestante

saldo = float(input("Digite o seu saldo: "))
saque = float(input("Digite o valor que você quer sacar: "))

print(saldoFinal(saldo, saque))