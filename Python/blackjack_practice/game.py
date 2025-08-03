import pygame
import random
import os
import time

pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Blackjack")

GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Card values
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
suit_symbols = {
    's': '♠',  # Spades
    'h': '♥',  # Hearts
    'd': '♦',  # Diamonds
    'c': '♣'   # Clubs
}
rank_name = {
    '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
    '7': '7', '8': '8', '9': '9', '10': '10',
    'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'
}

font = pygame.font.SysFont(None,36)


# Card and Deck Classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = ranks[rank]
        self.image = os.path.join("assets", f"{rank_name[self.rank]}_of_{self.suit}.png")

    def __str__(self):
        return f"{self.rank}{suit_symbols[self.suit[0]]}"
    
    def get_image(self, scale=(100,140)):
        image = pygame.image.load(self.image).convert_alpha()
        return pygame.transform.scale(image,scale)


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in suits for r in ranks] * 6
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def remaining(self):
        return len(self.cards)
    
    def shuffle(self):
        self.cards = [Card(s, r) for s in suits for r in ranks] * 6
        random.shuffle(self.cards)
        
    def print(self):
        for x in self.cards:
            print(x)
        print(len(self.cards))


# Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.aces += 1
        self.adjust_aces()
        
    def remove_cards(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
    def print(self):
        for x in self.cards:
            print(x)
            
    def isPair(self):
        if(len(self.cards) > 2):
            return False
        elif(self.cards[0].value == self.cards[1].value):
            return True
        else:
            return False
            
def deal(player, dealer):
    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        
def clear_table(player, dealer):
    player.remove_cards()
    dealer.remove_cards()
        
def draw_text(text,x,y):
    img = font.render(text, True, WHITE)
    screen.blit(img,(x,y))
        
def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, BLACK, (x,y,w,h))
    draw_text(text, x + 10, y + 10)
    return pygame.Rect(x,y,w,h)
        
def draw_player_hand(player):
    draw_text(f"Player Hand: {player.value}",50,50)
    for i, card in enumerate(player.cards):
        img = card.get_image()
        screen.blit(img, (50 + i*30,100 + i*10))
        
def draw_dealer_hand(dealer, player=True):
    if player:
        value = dealer.cards[0].value
    else:
        value = dealer.value
    draw_text(f"Dealer Hand: {value}",640,50)
    for i, card in enumerate(dealer.cards):
        if(player and i == 0):
            img = card.get_image()
            screen.blit(img, (640,100))
        elif(player and i == 1):
            pygame.draw.rect(screen, "gray", (750, 100, 100, 140))
        elif(not player):
            img = card.get_image()
            screen.blit(img, (640 + i*110,100))
            
def should_split(card, dealer):
    if(card.rank == 'A'):
        return True
    if(card.value == 10):
        return False
    if(card.rank == '9'):
        if dealer.rank not in ['7', 'J', 'Q','K', 'A']:
            return True
        return False
    if(card.rank == '8'):
        return True
    if(card.rank == '7'):
        if dealer.rank not in ['8','9', 'J', 'Q','K', 'A']:
            return True
        return False
    if(card.rank == '6'):
        if dealer.rank not in ['7','8','9', 'J', 'Q','K', 'A']:
            return True
        return False
    if(card.rank == '5'):
        return False
    if(card.rank == '4'):
        if dealer.rank in ['5','6']:
            return True
        return False
    if(card.rank == '3'):
        if dealer.rank not in ['8','9', 'J', 'Q','K', 'A']:
            return True
        return False
    if(card.rank == '2'):
        if dealer.rank not in ['8','9', 'J', 'Q','K', 'A']:
            return True
        return False
    return False

def soft_action(value, dealer):
    if value == 9:
        return "S"
    if value == 8:
        if dealer.rank in ['6']:
            return "D"
        return "S"
    if value == 7:
        if dealer.rank in ['2','3','4','5','6']:
            return "D"
        if dealer.rank in ['7','8']:
            return "S"
        return "H"
    if value == 6:
        if dealer.rank in ['3','4','5','6']:
            return "D"
        return "H"
    if value in [5, 4]:
        if dealer.rank in ['4','5','6']:
            return "D"
        return "H"
    if value in [3, 2]:
        if dealer.rank in ['5','6']:
            return "D"
        return "H"
    
def hard_action(value, dealer):
    if value >= 17:
        return "S"
    if value < 17 and value > 12:
        if dealer.rank in ['2','3','4','5','6']:
            return "S"
        return "H"
    if value == 12:
        if dealer.rank in ['4','5','6']:
            return "S"
        return "H"
    if value == 11:
        return "D"
    if value == 10:
        if dealer.rank in ['J','Q','K','A']:
            return "H"
        return "D"
    if value == 9:
        if dealer.rank in ['3','4','5','6']:
            return "D"
        return "H"
    if value <= 8:
        return "H"
    

# Game State
deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

result = ""

lobby = True
playing = False
player = False
round_over = False
can_split = False
can_double = False

action = ""

running = True
while running:
    screen.fill(GREEN)
    
    if(len(player_hand.cards) <= 2):
        can_double = True
    else:
        can_double = False
        
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            mouse_pos = event.pos
            
            if lobby and play_button.collidepoint(mouse_pos):
                lobby = False
                playing = True
                player = True
                clear_table(player_hand, dealer_hand)
                deal(player_hand, dealer_hand)
                
                action = ""
                
                if(player_hand.isPair()):
                    can_split = True
                    if should_split(player_hand.cards[0], dealer_hand.cards[0]):
                        action = "split"
                
                value_without_aces = 0
                for card in player_hand.cards:
                    if card.rank != 'A':
                        value_without_aces += card.value
                
                if(player_hand.aces > 0 and not action):
                    if soft_action(value_without_aces, dealer_hand.cards[0]) == 'D':
                        action = "double"
                    if soft_action(value_without_aces, dealer_hand.cards[0]) == 'H':
                        action = "hit"
                    if soft_action(value_without_aces, dealer_hand.cards[0]) == 'S':
                        action = "stand"
                        
                if not action:
                    if hard_action(player_hand.value, dealer_hand.cards[0]) == 'D':
                        action = "double"
                    if hard_action(player_hand.value, dealer_hand.cards[0]) == 'H':
                        action = "hit"
                    if hard_action(player_hand.value, dealer_hand.cards[0]) == 'S':
                        action = "stand"

                print(action)
                
                if(dealer_hand.value == 21 or player_hand.value == 21):
                    playing = False
                    player = False
                    round_over = True
                    pygame.display.flip()
    
            elif playing:
                if hit_button.collidepoint(mouse_pos):
                    player_hand.add_card(deck.deal())
                    if(player_hand.value > 21):
                        player = False
                        playing = False
                        round_over = True
                        can_split = False
                        continue
                    
                    action = ""
                    
                    value_without_aces = 0
                    for card in player_hand.cards:
                        if card.rank != 'A':
                            value_without_aces += card.value
                    
                    if(player_hand.aces > 0 and not action):
                        if soft_action(value_without_aces, dealer_hand.cards[0]) == 'D':
                            if value_without_aces in [7, 8]:
                                action = "stand"
                            else:
                                action = "hit"
                        if soft_action(value_without_aces, dealer_hand.cards[0]) == 'H':
                            action = "hit"
                        if soft_action(value_without_aces, dealer_hand.cards[0]) == 'S':
                            action = "stand"
                            
                    if not action:
                        if hard_action(player_hand.value, dealer_hand.cards[0]) == 'D':
                            action = "hit"
                        if hard_action(player_hand.value, dealer_hand.cards[0]) == 'H':
                            action = "hit"
                        if hard_action(player_hand.value, dealer_hand.cards[0]) == 'S':
                            action = "stand"

                    print(action)
                    
                elif stand_button.collidepoint(mouse_pos):
                    player = False
                    while(dealer_hand.value < 17 or (dealer_hand.value == 17 and dealer_hand.aces > 0)):
                        screen.fill(GREEN)
                        draw_dealer_hand(dealer_hand,player)
                        draw_player_hand(player_hand)
                        pygame.display.flip()
                        time.sleep(0.5)
                        dealer_hand.add_card(deck.deal())
                    round_over = True
                    playing = False
                    can_split = False
                elif can_split and split_button.collidepoint(mouse_pos):
                    pass
                elif double_button.collidepoint(mouse_pos):
                    player_hand.add_card(deck.deal())
                    player = False
                    if(player_hand.value > 21):
                        round_over = True
                        playing = False
                        can_split = False
                        round_over = True
                        continue
                    while(dealer_hand.value < 17 or (dealer_hand.value == 17 and dealer_hand.aces > 0)):
                        screen.fill(GREEN)
                        draw_dealer_hand(dealer_hand,player)
                        draw_player_hand(player_hand)
                        pygame.display.flip()
                        time.sleep(0.5)
                        dealer_hand.add_card(deck.deal())
                    playing = False
                    can_split = False
                    round_over = True
                    
                    
            
            elif round_over:
                if again_button.collidepoint(mouse_pos):
                    action = ""
                    round_over = False
                    playing = True
                    player = True
                    clear_table(player_hand, dealer_hand)
                    deal(player_hand, dealer_hand)
                    
                    if(player_hand.isPair()):
                        can_split = True
                        if should_split(player_hand.cards[0], dealer_hand.cards[0]):
                            action = "split"
                    
                    value_without_aces = 0
                    for card in player_hand.cards:
                        if card.rank != 'A':
                            value_without_aces += card.value
                    
                    if(player_hand.aces > 0 and not action):
                        if soft_action(value_without_aces, dealer_hand.cards[0]) == 'D':
                            action = "double"
                        if soft_action(value_without_aces, dealer_hand.cards[0]) == 'H':
                            action = "hit"
                        if soft_action(value_without_aces, dealer_hand.cards[0]) == 'S':
                            action = "stand"
                            
                    if not action:
                        if hard_action(player_hand.value, dealer_hand.cards[0]) == 'D':
                            action = "double"
                        if hard_action(player_hand.value, dealer_hand.cards[0]) == 'H':
                            action = "hit"
                        if hard_action(player_hand.value, dealer_hand.cards[0]) == 'S':
                            action = "stand"

                    print(action)
                    
                    if(dealer_hand.value == 21 or player_hand.value == 21):
                        playing = False
                        player = False
                        round_over = True
                        
    
                
        
    if(lobby):
         play_button = draw_button("Play", 640, 360, 100, 40)
    elif(not lobby):
        
        # Draw Player Hand
        draw_player_hand(player_hand)
            
        # Draw Dealer Hand
        draw_dealer_hand(dealer_hand,player)
            
        if(player):
            hit_button = draw_button("Hit", 100, 500, 100, 40)
            stand_button = draw_button("Stand", 220, 500, 100, 40)
            if(can_double):
                double_button = draw_button("Double", 220, 550, 100, 40)
            if(can_split):
                split_button = draw_button("Split", 100, 550, 100, 40)
            
            
    if(round_over):
        again_button = draw_button("Again", 100, 600, 100, 40)
        
    
    
    pygame.display.flip()

pygame.quit()