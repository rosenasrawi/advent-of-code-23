from _getinput import *
from collections import Counter

# --- Day 7: Camel Cards ---

def card2nums(card):

    card_nums = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

    card = [card_nums[c] if c in card_nums else int(c) for c in card]

    return card

def get_cards():

    input = getinput(day='07', example=False)
    input = [line.split() for line in input]

    cards = [card2nums(list(card)) for card, _ in input]
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

def sort_cards():

    cards, bids = get_cards()
    hands = [check_hand(card) for card in cards]
    cards = list(zip(hands, bids, cards))
    cards = list(sorted(cards, key=lambda x:x[0], reverse=True))

    cards_sorted = []

    for i, card in enumerate(cards):
        
        cards_sorted.append(card)

        if len(cards_sorted) != 1:

            move = i
            in_place = False

            while not in_place:

                hp, bp, cp = cards_sorted[move-1]
                hn, bn, cn = cards_sorted[move]

                if hp > hn: # never past another hand
                    break

                if hp == hn: # same hand, then compare

                    for j in range(len(cp)):
                        if cp[j] < cn[j]: # switch cards
                            cards_sorted[move-1] = [hn, bn, cn]
                            cards_sorted[move] = [hp, bp, cp]
                            break
                        elif cp[j] > cn[j]:
                            break
                    
                move -= 1

                if move == 0: break

    return cards_sorted

def get_ranks():

    cards_sorted = sort_cards()

    bid_multiply = list(range(len(cards_sorted), 0, -1))
    bids = [b for _, b, _ in cards_sorted]

    total = 0

    for i, b in enumerate(bids):
        total += b*bid_multiply[i]

    return total

print('Part 1:', get_ranks())