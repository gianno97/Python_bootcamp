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

    def initial_cards(self):
        self.four_cards = []
        
        for i in range(4):
            self.four_cards.append(self.all_cards.pop(0))

        return self.four_cards

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

        while(True):
            if(bet > 0 and bet <= new_amount.amount):
                print("OK!")
                break
            else:
                print("Valore non valido!")
                bet = int(input("Fai una puntata "))
        
        new_deck = Deck()
        new_deck.shuffle()
        init_cards = new_deck.initial_cards()
        dealer_cards = init_cards[0:2]
        player_cards = init_cards[2:4]
        print("Carte del dealer:\n", dealer_cards[0], "\nUna carta coperta")
        print("Carte del giocatore:\n", player_cards[0], "\n", player_cards[1])
        total_player = 0
        total_dealer = 0

        for card_player in player_cards:
                    total_player += card_player.value

        while(True):
            action = input("1.Chiedi una carta\n2.Fermati\n")

            if(action == "1"):
                total_player = 0
                player_cards.append(new_deck.hit())

                for card_player in player_cards:
                    total_player += card_player.value
                
                if(total_player == 21):
                    print("Blackjack! Il giocatore ha vinto")
                    break
                elif(total_player < 21):
                    print("Carte del giocatore:\n")
                    for card_player in player_cards:
                        print(card_player)
                    continue
                else:
                    print("La somma è", total_player, "Il giocatore ha perso")
                    break
            elif(action == "2"):
                while(True):
                    total_dealer = 0
                    for card_dealer in dealer_cards:
                        total_dealer += card_dealer.value
                    
                    print(total_dealer)
                    print("Carte del dealer:")
                    for card_dealer in dealer_cards:
                        print(card_dealer)

                    if(total_dealer == 21):
                        print("Blackjack! Il dealer ha vinto")
                        break
                    elif(total_dealer <= total_player):
                        dealer_cards.append(new_deck.hit())
                    else:
                        if(total_dealer <= 21):
                            print("Il dealer ha vinto")
                            break
                        else:
                            print("Il giocatore ha vinto")
                            break
            else:
                print("Valore non valido")
            break
    elif(x == "2"):
        print("Gioco concluso!")
        game_on = False
    else:
        print("Valore non valido!")
        

