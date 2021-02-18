from random import randint


# Variáveis
jogador_1 = [[100]]  # [HP[0], [Ataque[0], defesa[1] sorte[2]]]
jogador_2 = [[100]]
teste = False
atributos = 30
contador = 0
jogador = 0


# Ataque + Defesa + Sorte = 30
# Max Atak or max def or max sor = 20


# While para caso o valor digitado seja inválido
while teste == False:
    while teste == False:  # Este segundo while é específico para a escolha dos pontos do personagem
        print('Criação do personagem. Você possui 30 pontos para dividir entre ataque, defesa e sorte')
        ataque = int(input('Escolha um valor para Ataque entre 1 e 20: '))
        if ataque >= 1 and ataque <= 20:
            defesa = int(input(f'Escolha um valor para Defesa entre 1 e {atributos - ataque}: '))
            if defesa >= 1 and defesa <= (atributos - ataque):
                sorte = atributos - ataque - defesa
                print(f'sobraram {sorte} pontos de Sorte\n\n')
                teste = True  # Neste momento ele passa para o primeiro while
                # Os valores ainda não foram adicionados ao jogador 1 para evitar duplicata caso o jogador
                # Escolha valores inválidos na próxima questão
            else:
                print('ERRO. Um atributo precisa ter ao menos 1 ponto e no máximo 20. A soma de todos os atributos precisa ser 30')
            
            
    print('Digite o número equivalente ao oponente tipo de oponente que deseja lutar\n\n1 - Balanceado: Ataque = 10, Defesa = 10, Sorte = 10')
    print('2 - Ofensivo: Ataque = 15, Defesa = 5, Sorte = 10\n3 - Defensivo: Ataque = 5, Defesa = 15, Sorte = 10')
    escolha_oponente = int(input('4 - Sortudo: Ataque = 5, Defesa = 5, Sorte = 20\n'))
    
    # Adicionando uma nova lista com 3 valores e utilizando o teste para entrar ou sair do loop
    if escolha_oponente >= 1 and escolha_oponente <= 4:
        if escolha_oponente == 1:
            jogador_2.append([10, 10, 10])

        elif escolha_oponente == 2:
            jogador_2.append([15, 5, 10])

        elif escolha_oponente == 3:
            jogador_2.append([5, 15, 10])

        elif escolha_oponente == 4:
            jogador_2.append([5, 5, 20])
        jogador_1.append([ataque, defesa, sorte])

    else:
        teste = False  # Retorna para o começo do código (primeiro while)
        print('Oponente inválido')




        
# Instruções
print('\nCada jogador terá uma ação por turno, escolhendo entre uma manobra arriscada ou conservadora.', end=' ')
print('No caso do movimento arriscado, seu poder de Ataque é dobrado apenas neste instante.', end=' ')
print('No caso do movimento conservador, seu poder de Defesa é temporariamente dobrado.')
print('Tem uma chance de causar 10 de dano extra (crítico) conforme o seu nível de Sorte.', end=' ')
print('É feito o sorteio de um número aleatório entre 1 e 20 e se o parâmetro de Sorte for maior do que o valor sorteado,', end=' ')
print('então o Jogador 2 sofrerá esse ataque crítico, que é independente do que aconteceu no item anterior.')


# Variáveis usadas para duplicar defesa ou ataque e depois retornar ao estado inicial (acampar com o efeito temporário)
ataque_1 = jogador_1[1][0]
ataque_2 = jogador_2[1][0]
defesa_1 = jogador_1[1][1]
defesa_2 = jogador_2[1][1]


# laço que repetirá enquanto um deles estiver vivo
while jogador_1[0][0] > 0 and jogador_2[0][0] > 0:
    contador += 1
    print('\n\n\t\t{}\n\t\t{} ROUND {} {}\n\t\t{}'.format(29 * '*', 10 * '*', contador, 10 * '*', 29 * '*'))
    print(f'Saúde atual do Jogador 1: {jogador_1[0][0]}\t\tSaúde atual do Jogador 2: {jogador_2[0][0]}\n\n')
    # Esse if serve pra poder fazer a interpolação entre 2 números
    if jogador == 1:
        jogador = 2
    else:
        jogador = 1
    print(f'\t\t\t-----Jogador {jogador}-----')

    critico = 0
    def ataque_jogador_1(dano):
        jogador_2[0][0] -= dano
        print(f'Dano causado : {dano}')
        defesa_2 = jogador_2[1][1]  # Caso o jogador tenha escolhido defesa, o escudo expira neste momento
        
    def ataque_jogador_2(dano):
        jogador_1[0][0] -= dano
        print(f'Dano causado : {dano}')
        defesa_1 = jogador_1[1][1] 

    if jogador == 1:
        manobra = int(input('Escolha a manobra:\n1 - Ataque\n2 - Defesa\n'))
    else:
        manobra = randint(1, 2)
    
    
    if jogador == 1:  # Usando a variável jogador para alternar as jogadas
        if defesa_1 == (jogador_1[1][1] * 2):  # Resetando a defesa para não acumular caso nenhum dos dois tenha escolhido ataque
            defesa_1 = jogador_1[1][1]
        if manobra == 1:
            if (ataque_1 * 2) > defesa_2:  # Checa se terá dano para iniciar a função de ataque
                ataque_jogador_1(ataque_1 * 2 - defesa_2)
            if jogador_1[1][2] > randint(1, 20):  # Checa se haverá um dano crítico ou não
                print('O jogador 2 recebeu um dano crítico')
                jogador_2[0][0] -= 10
        elif manobra == 2:
            defesa_1 *= 2
            print(f'Sua defesa aumentou para {defesa_1}')
            if jogador_1[1][2] > randint(1, 20):  # Precisei checar o crítico aqui novamente
                print('O jogador 2 recebeu um dano crítico')
                jogador_2[0][0] -= 10
        else:
            print('ERRO. Escolha inválida.')  # Colocando um while nesse bloco, dá pra fazer essa escolha errada dar uma nova chance
                                              # De escolha, mas eu não o fiz.

                
    # Aqui o código se repete para o jogador 2
    else:
        if defesa_2 == (jogador_2[1][1] * 2):
            defesa_2 = jogador_2[1][1]
        if manobra == 1:
            if (ataque_2 * 2) > defesa_1:
                ataque_jogador_2(ataque_2 * 2 - defesa_1)
            if jogador_2[1][2] > randint(1, 20):
                print('O jogador 1 recebeu um dano crítico')
                jogador_1[0][0] -= 10
            
        elif manobra == 2:
            defesa_2 *= 2
            print(f'Sua defesa aumentou para {defesa_2}')
            if jogador_2[1][2] > randint(1, 20):
                print('O jogador 1 recebeu um dano crítico')
                jogador_1[0][0] -= 10
        else:
            print('ERRO. Escolha inválida.')


# Indica o vencedor
if jogador_1[0][0] <= 0:
    print('O jogador 2 foi o vencedor!')
if jogador_2[0][0] <= 0:
    print('O jogador 1 foi o vencedor!')