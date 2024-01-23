import pygame
import sys
import random


pygame.init()

# Skjermstørrelse
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


font = pygame.font.Font(None, 36)

# Hender
player_hand = []
dealer_hand = []

# $$$$$
bet = 10
total_money = 1000


result_message = ""

# Nytt spill
def start_new_game():
    global player_hand, dealer_hand, result_message
    player_hand = [get_card(), get_card()]
    dealer_hand = [get_card(), get_card()]
    result_message = ""

# Nytt kort
def get_card():
    return random.randint(1, 11)

# Tegn
def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Kort tegn
def draw_cards(hand, y):
    x = 50
    for card in hand:
        pygame.draw.rect(screen, WHITE, (x, y, 50, 80))
        draw_text(str(card), x + 20, y + 30, BLACK)
        x += 60

# Check hånd under 21
def is_bust(hand):
    return sum(hand) > 21

# Winner check
def determine_winner(player, dealer):
    if is_bust(player):
        return "Dealer Wins!"
    elif is_bust(dealer):
        return "Player Wins!"
    elif sum(player) > sum(dealer):
        return "Player Wins!"
    elif sum(player) < sum(dealer):
        return "Dealer Wins!"
    else:
        return "It's a Tie!"

# main løkke
def game_loop():
    global bet, total_money, result_message
    start_new_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # klikk
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # HIT
                if 200 < mouse_x < 300 and 500 < mouse_y < 550:
                    player_hand.append(get_card())

                # STAND
                elif 350 < mouse_x < 450 and 500 < mouse_y < 550:
                    # Dealer trekk
                    while sum(dealer_hand) < 17:
                        dealer_hand.append(get_card())

                    winner_text = determine_winner(player_hand, dealer_hand)
                    total_money += bet if winner_text.startswith("Player") else -bet
                    result_message = winner_text
                    start_new_game()

        # Bakgrunn
        screen.fill(RED)

        # Spiller kort
        draw_cards(player_hand, 400)

        # Dealer kort (kun et vises)
        draw_cards([dealer_hand[0], "X"], 100)

        # Bet
        draw_text("Bet: $" + str(bet), 50, 50, BLACK)

        # BUtooons
        pygame.draw.rect(screen, WHITE, (200, 500, 100, 50))  # Hit
        pygame.draw.rect(screen, WHITE, (350, 500, 100, 50))  # Stand

        draw_text("Hit", 235, 515, BLACK)
        draw_text("Stand", 365, 515, BLACK)

        # Spillerens money
        draw_text("Total Money: $" + str(total_money), 530, 50, BLACK)

        # Result prompt
        draw_text(result_message, 300, 250, WHITE)

      
        pygame.display.flip()


game_loop()
