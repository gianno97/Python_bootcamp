import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit 

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def hit(self):
        return self.all_cards.pop(0)

class Player:
    def __init__(self, name):
        self.name = name

class Cash:
    def __init__(self, amount):
        self.amount = amount


game_on = True

print("Gioco del Blackjack testuale:")

while(game_on):
    # print("1.Gioca\n2.Esci")
    # fsjkajdfkajfkd
    x = input("1.Gioca\n2.Esci\n")

    if(x == "1"):
        new_player = Player(input("Inserisci nome giocatore: "))
        new_amount = Cash(100)
        print(new_player.name + " hai a disposizione", new_amount.amount)
        bet = int(input("Fai una puntata "))
        if(bet <= new_amount.amount):
            print("OK!")
        else:
            print("Fondi insufficenti!")  
    elif(x == "2"):
        print("Gioco concluso!")
        game_on = False
    else:
        print("Valore non valido!")
        

