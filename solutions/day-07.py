from _getinput import *
from collections import Counter
from itertools import product

# --- Day 7: Camel Cards ---

def card2nums(card, joker = False):

    card_nums = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

    if joker: card_nums['J'] = 0

    card = [card_nums[c] if c in card_nums else int(c) for c in card]

    return card

def get_cards(joker = False):

    input = getinput(day='07', example=False)
    input = [line.split() for line in input]

    cards = [card2nums(list(card),joker) for card, _ in input]
    bids = [int(bid) for _, bid in input]

    return cards, bids

def check_hand(card):

    counts = Counter(card)
    hand_type = list(range(7,0,-1))
    
    match = [
        any(count == 5 for count in counts.values()),
        any(count == 4 for count in counts.values()),
        set(counts.values()) == {2, 3},
        any(count == 3 for count in counts.values()) and len(counts) == 3,
        list(counts.values()).count(2) == 2,
        2 in counts.values() and len(counts) == 4,
        len(counts) == 5,
    ]

    return hand_type[match.index(True)]

def check_joker(card):
    best_hand = 0

    jokers = [i for i, c in enumerate(card) if c == 0]
    sub_options = list(product(range(2, 15), repeat=len(jokers)))

    for sub in sub_options:
        sub_card = card.copy()
        
        for j, s in zip(jokers, sub):
            sub_card[j] = s
        
        hand = check_hand(sub_card)
        
        if hand > best_hand:
            best_hand = hand
    
    return best_hand

def get_hands(joker = False):

    cards, bids = get_cards(joker)
    hands = []

    for card in cards:
        if joker and 0 in card:
            hands.append(check_joker(card))
        else:
            hands.append(check_hand(card))

    cards = list(zip(hands, bids, cards))
    cards = list(sorted(cards, key=lambda x:x[0], reverse=True))    

    return cards, bids

def sort_cards(joker = False):

    cards, bids = get_hands(joker)
    cards_sorted = []

    for i, card in enumerate(cards):
        
        cards_sorted.append(card)

        if len(cards_sorted) != 1:

            move = i

            while True:

                hp, bp, cp = cards_sorted[move-1]
                hn, bn, cn = cards_sorted[move]

                if hp > hn:
                    break

                if hp == hn:

                    for j in range(len(cp)):
                        if cp[j] < cn[j]:
                            cards_sorted[move-1] = [hn, bn, cn]
                            cards_sorted[move] = [hp, bp, cp]
                            break
                        elif cp[j] > cn[j]:
                            break
                    
                move -= 1
                if move == 0: break

    bid_multiply = list(range(len(cards_sorted), 0, -1))
    bids = [b for _, b, _ in cards_sorted]

    total = 0

    for i, b in enumerate(bids):
        total += b*bid_multiply[i]

    return total

print('Part 1:', sort_cards())
print('Part 2:', sort_cards(joker=True))