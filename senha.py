erro = 0

while True:
    senha = int(input('digite sua senha:'))
    
    if senha == 1234:
        print('Login efetuado com sucesso')
    else:
        print('Erro ao fazer o login, tente novamente!')
        erro = erro + 1
        print(f'Você errou {erro}x')
        continue
    break