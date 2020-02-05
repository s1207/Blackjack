import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suits, ranks):
        self.suit = suits
        self.rank = ranks

    def __str__(self):
        return self.rank + ' of ' + self.suits


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                c = Card(rank, suit)
                self.deck.append(c)

    def __str__(self):
        for card in self.deck:
            print(card.rank + ' of ' + card.suit)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values.get(card.rank)

    def adjust_for_ace(self):
        if self.value == 10:
            self.value += 11
        elif self.value == 20:
            self.value += 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet*2

    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    while True:
        try:
            bet = int(input('Please enter the amount you want to bet: '))
        except:
            print ("That's not an integer")
            continue
        else:
            print("You are betting ", bet)
            break


def hit(deck, hand):
    c = (deck.deck.deal())
    hand.cards.append(c)
    if c.rank == 'Ace':
        hand.adjust_for_ace()


def hit_stand(deck, hand):
    global playing
    player_input = input("DO you want to hit or pass? Enter H or P :")
    if player_input == "H":
        hit(deck, hand)
    else:
        playing = False


def show_more(player, dealer):
    for card in player.cards:
        print(card.rank + "of" + card.suit)
    for card in dealer.cards:
        index =0
        if index == 0:
            continue
        else:
            print(card.rank + "of" + card.suit)


def show_all(player, dealer):
    pass


def player_busts(hand, chips):
    if hand.value > 21:
        chips.lose_bet()
        return True
    else:
        return False


def player_wins(player, dealer, chips):
    if player.value == 21:
        return True
    elif player.value < 21:
        if player.value > dealer.value:
            return True
    else:
        return False


def dealer_wins(player, dealer, chips):
    if dealer.value == 21:
        return True
    elif dealer.value < 21:
        if dealer.value > player.value:
            return True
    else:
        return False


def dealer_busts(hand, chips):
    if hand.value > 21:
        return True
    else:
        return False


def push(player, dealer):
    if player.value == dealer.value:
        return True
    else:
        return False


while True:

    print('Welcome to BlackJack!!!')
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())






