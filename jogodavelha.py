import pygame
import sys
import math

# Cores do Jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Setup da tela do Jogo
window = pygame.display.set_mode((600, 600))
window.fill(branco)

# Grade do tabuleiro 
pygame.draw.line(window, preto, (205, 50), (205, 521), 10)
pygame.draw.line(window, preto, (365, 50), (365, 521), 10)
pygame.draw.line(window, preto, (50, 205), (521, 205), 10)
pygame.draw.line(window, preto, (50, 365), (521, 365), 10)

# Declarando estado X ou O - Onde (1 = X) e (0 = O)
x_ou_o = 1
position = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Declarando traço final
fim = 0

def minimax(position, depth, maximizingPlayer):
    winner = check_winner(position)
    if winner == 1:
        return 10 - depth
    elif winner == 2:
        return depth - 10
    elif is_board_full(position):
        return 0  # Empate

    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(9):
            if position[i] == 0:
                position[i] = 1
                eval = minimax(position, depth + 1, False)
                position[i] = 0
                maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for i in range(9):
            if position[i] == 0:
                position[i] = 2
                eval = minimax(position, depth + 1, True)
                position[i] = 0
                minEval = min(minEval, eval)
        return minEval


def is_board_full(position):
    return all(p != 0 for p in position)


def check_winner(position):
    for i in range(3):
        if position[i*3] == position[i*3+1] == position[i*3+2] != 0:
            return position[i*3]
        if position[i] == position[i+3] == position[i+6] != 0:
            return position[i]
    if position[0] == position[4] == position[8] != 0:
        return position[0]
    if position[2] == position[4] == position[6] != 0:
        return position[2]
    return 0

def machine_play(position):
    # Verifica primeiro se a máquina pode ganhar na próxima jogada
    for i in range(9):
        if position[i] == 0:
            position[i] = 1  # Movimento da máquina
            if check_winner(position) == 1:
                return i  # Vence o jogo
            position[i] = 0

    # Se a máquina não pode ganhar, então bloqueia o oponente
    for i in range(9):
        if position[i] == 0:
            position[i] = 2  # Movimento do oponente
            if check_winner(position) == 2:
                position[i] = 0
                return i  # Bloqueia o oponente
            position[i] = 0

    # Se não há jogadas vencedoras ou bloqueios, escolhe a melhor jogada
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if position[i] == 0:
            position[i] = 1
            score = minimax(position, 0, False)
            position[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    return best_move



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    if x_ou_o == 0 and fim == 0:
        # Máquina joga
        move = machine_play(position)
        if move != -1:
            row = move // 3
            col = move % 3
            x = 50 + col * 161
            y = 50 + row * 161
            pygame.draw.line(window, vermelho, (x + 50, y + 50), (x + 100, y + 100), 10)
            pygame.draw.line(window, vermelho, (x + 100, y + 50), (x + 50, y + 100), 10)
            position[move] = 1
            x_ou_o = 1

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Verifica se houve clique em um quadrado vazio e realiza a jogada do jogador
    if click[0] == 1 and fim == 0:
        if 50 <= mouse[0] <= 200 and 50 <= mouse[1] <= 200 and position[0] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (125, 125), 50, 10)
            position[0] = 2
            x_ou_o = 0
        elif 211 <= mouse[0] <= 360 and 50 <= mouse[1] <= 200 and position[1] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (286, 125), 50, 10)
            position[1] = 2
            x_ou_o = 0
        elif 371 <= mouse[0] <= 520 and 50 <= mouse[1] <= 200 and position[2] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (446, 125), 50, 10)
            position[2] = 2
            x_ou_o = 0
        elif 50 <= mouse[0] <= 200 and 211 <= mouse[1] <= 361 and position[3] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (125, 286), 50, 10)
            position[3] = 2
            x_ou_o = 0
        elif 211 <= mouse[0] <= 360 and 211 <= mouse[1] <= 361 and position[4] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (286, 286), 50, 10)
            position[4] = 2
            x_ou_o = 0
        elif 371 <= mouse[0] <= 520 and 211 <= mouse[1] <= 361 and position[5] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (446, 286), 50, 10)
            position[5] = 2
            x_ou_o = 0
        elif 50 <= mouse[0] <= 200 and 371 <= mouse[1] <= 521 and position[6] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (125, 447), 50, 10)
            position[6] = 2
            x_ou_o = 0
        elif 211 <= mouse[0] <= 360 and 371 <= mouse[1] <= 521 and position[7] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (286, 447), 50, 10)
            position[7] = 2
            x_ou_o = 0
        elif 371 <= mouse[0] <= 520 and 371 <= mouse[1] <= 521 and position[8] == 0 and x_ou_o == 1:
            pygame.draw.circle(window, azul, (446, 447), 50, 10)
            position[8] = 2
            x_ou_o = 0

    # Verifica se houve vencedor ou empate
    winner = check_winner(position)
    if winner == 1 or winner == 2 or sum(position) == 14:
        fim = 1
  
    pygame.display.update()