# Advinhação com pontuação.
# Quanto + distante do nº secreto, + pontos perde.

import random

opcao_jogar_novamente = 'Sim'

while opcao_jogar_novamente == 'Sim':
    print('*' * 37)
    print('Bem vindo ao jogo de advinhação')
    print('*' * 37)
    print('\nEscolha o nível do jogo:     [1] Fácil     [2] Médio     [3] Difícil')

    pontos = 1000

    opcao = int(input('Digite o número da opção:'))
    while opcao < 1 or opcao > 3:
        print('Digite um número válido')
        opcao = int(input('Digite o número da opção:'))
    if opcao == 1:
        total_de_tentativas = 7
    elif opcao == 2:
        total_de_tentativas = 5
    elif opcao == 3:
        total_de_tentativas = 3
    print('Você tem {} tentativas e {} pontos.'.format(total_de_tentativas, pontos))

    numero_secreto = round(random.randrange(1, 101))

    for rodada in range(1, total_de_tentativas + 1):
        print('\nEsta é a rodada {} de {}.'.format(rodada, total_de_tentativas))
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou {}...'.format(chute))
        acertou = chute == numero_secreto
        menor = chute > numero_secreto
        maior = chute < numero_secreto

        if (chute < 1) or (chute > 100):
            print('Chute um valor de 1 a 100')
            continue

        if acertou:
            print('\nVocê acertou! \n ¯\_( ͡◡ ͜ʖ ͡◡)_/¯')
            break
        else:
            if menor:
                print('\nNúmero secreto é menor do que o chutado.')
                pontos_perdidos = chute - numero_secreto
            elif maior:
                print('\nNúmero secreto é maior do que o chutado.')
                pontos_perdidos = numero_secreto - chute
            pontos = pontos - (pontos_perdidos * 3)
    print('Fim do Jogo.\nO número secreto é {} e sua pontuação foi de.... {} Pontos.'.format(numero_secreto, pontos))
# Ou usar função abs para módulo: abs()
# pontos_perdidos = abs(chute - numero_secreto)

    if pontos <= 500:
        print('Você foi bem mal :( Mais sorte na próxima!')
    elif pontos > 500 and pontos <= 700:
        print('Você foi bem! Mas pode ir melhor ein!')
    elif pontos > 700 and pontos <= 999:
        print('Arrasou!')
    elif pontos == 1000:
        print('DE PRIMEIRAAA!! TOP DEMAIS!')

    print('Jogar de novo?\n    [Sim]\n    [Não]')
    opcao_jogar_novamente = str(input())
    if opcao_jogar_novamente == 'Não':
        continue
    elif opcao_jogar_novamente == 'Sim':
        continue
    else:
        opcao_jogar_novamente = str(input('Digite um valor válido: '))
