def verificarAcesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Acesso bloqueado!"
    
    if usuario == "admin" and senha == "1234":
        return "Acesso total"
    elif usuario == "admin" and senha != "1234":
        return "Senha incorreta!"
    else:
        return "Usuário inválido!"
    
usuario = input("Digite o usuário: ")
senha = input("Digite a senha:")
tentativas = int(input("Digite a quantidade de tentativas: "))

print(verificarAcesso(usuario, senha, tentativas))