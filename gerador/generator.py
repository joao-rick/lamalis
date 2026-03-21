import random

def geraCoin():
    n_coin = 1

    especiais = [ '@', '$', '-', '?']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letras_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    coins = []
    i = 1
    t_coin = 9
    
    while i <= n_coin:
        coin = []
        
        while len(coin) < t_coin:
            t_coin = random.randint(3, 9)
            coin.append(random.choice(letras_mai))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(letras_mai))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(letras_mai))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(especiais))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(letras_min))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(letras_min))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(numeros))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(numeros))
            if len(coin) == t_coin:
                break
            coin.append(random.choice(numeros))
            if len(coin) == t_coin:
                break
            
        coins.append(coin)            
        i = i + 1
        
    return coins

    
coins_geradas = geraCoin()

def geraSigla(nome_criptomoeda=None):
    t_sigla = random.randint(2, 3)

    if nome_criptomoeda is None:
        nome_criptomoeda = ''.join(coins_geradas[0])

    return nome_criptomoeda[:t_sigla].upper()

def geraValorAtual():
    return round(random.uniform(0.01, 100000.00), 2)

def geraValorInicial():
    return round(random.uniform(0.01, 100000.00), 2)

def geraNivelRisco():
    niveis = ['Low', 'Moderate', 'High']
    return random.choice(niveis)

j = 1
for coin in coins_geradas:
    cripto = ''.join(coin)
    print(f'coin {j}: {cripto}')
    print(f'Sigla: {geraSigla()}')
    print(f'Valor Atual US$: {geraValorAtual()}')
    print(f'Valor Inicial US$: {geraValorInicial()}')
    print(f'Nível de Risco: {geraNivelRisco()} \n')
    j = j + 1