
#  File: Poker.py
#  Description: Accepts user input on number of players and simulates one random round of a Poker game

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 06/20/2019
#  Date Last Modified: 06/20/2019

import random


class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank=12, suit='S'):
        if rank in Card.RANKS:
            self.rank = rank
        else:
            self.rank = 12

        if suit in Card.SUITS:
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck(object):
    # constructor
    def __init__(self, num_decks=1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card
    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)


class Poker(object):
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards

        for i in range(num_players):
            hand = []
            self.all_hands.append(hand)

        # deal all the hands
        for j in range(self.numCards_in_Hand):
            for i in range(num_players):
                self.all_hands[i].append(self.deck.deal())

    # simulates the play of the game
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse=True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ': ' + hand_str)
        print()

        highest_hand = []
        hand_points = []  # points associated with that hand
        highest_hand.append(0)
        highest_hand.append(0)
        # find point values
        for i in range(len(self.all_hands)):
            if self.is_royal(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_royal(self.all_hands[i])[1])
                if 10 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(10)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_royal(self.all_hands[i])[0], i + 1])
                elif 10 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_royal(self.all_hands[i])[0], i + 1])
            elif self.is_straight_flush(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_straight_flush(self.all_hands[i])[1])
                if 9 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(9)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_straight_flush(self.all_hands[i])[0], i + 1])
                elif 9 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_straight_flush(self.all_hands[i])[0], i + 1])
            elif self.is_four_kind(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_four_kind(self.all_hands[i])[1])
                if 8 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(8)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_four_kind(self.all_hands[i])[0], i + 1])
                elif 8 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_four_kind(self.all_hands[i])[0], i + 1])
            elif self.is_full_house(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_full_house(self.all_hands[i])[1])
                if 7 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(7)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_full_house(self.all_hands[i])[0], i + 1])
                elif 7 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_full_house(self.all_hands[i])[0], i + 1])
            elif self.is_flush(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_flush(self.all_hands[i])[1])
                if 6 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(6)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_flush(self.all_hands[i])[0], i + 1])
                elif 6 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_flush(self.all_hands[i])[0], i + 1])
            elif self.is_straight(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_straight(self.all_hands[i])[1])
                if 5 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(5)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_straight(self.all_hands[i])[0], i + 1])
                elif 5 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_straight(self.all_hands[i])[0], i + 1])
            elif self.is_three_kind(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_three_kind(self.all_hands[i])[1])
                if 4 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(4)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_three_kind(self.all_hands[i])[0], i + 1])
                elif 4 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_three_kind(self.all_hands[i])[0], i + 1])
            elif self.is_two_pair(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_two_pair(self.all_hands[i])[1])
                if 3 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(3)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_two_pair(self.all_hands[i])[0], i + 1])
                elif 3 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_two_pair(self.all_hands[i])[0], i + 1])
            elif self.is_one_pair(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_one_pair(self.all_hands[i])[1])
                if 2 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(2)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_one_pair(self.all_hands[i])[0], i + 1])
                elif 2 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_one_pair(self.all_hands[i])[0], i + 1])
            elif self.is_high_card(self.all_hands[i])[0] != 0:
                print('Player ' + str(i + 1) + ': ' + self.is_high_card(self.all_hands[i])[1])
                if 1 > highest_hand[0]:
                    highest_hand.clear()
                    hand_points.clear()
                    highest_hand.append(1)
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_high_card(self.all_hands[i])[0], i + 1])
                elif 1 == highest_hand[0]:
                    highest_hand.append(i + 1)
                    hand_points.append([self.is_high_card(self.all_hands[i])[0], i + 1])
        print()

        # print who wins/ties
        if len(highest_hand) > 2:
            hand_points = sorted(hand_points, reverse=True)
            # print(hand_points)  # check if points are sorted correctly
            for player in hand_points:
                print('Player ' + str(player[1]) + ' ties.')
        else:
            print('Player ' + str(highest_hand[1]) + ' wins.')

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if not same_suit:
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if not rank_order:
            return 0, ''

        # determine the points
        points = 10 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15 ** 1
        points = points + hand[4].rank

        return points, 'Royal Flush'

    # determine if a hand is a straight flush
    def is_straight_flush(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if not same_suit:
            return 0, ''

        rank_order = True
        for i in range(len(hand) - 1):
            rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)

        if not rank_order:
            return 0, ''
        # determine the points
        points = 9 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3
        points = points + hand[2].rank * 15 ** 2 + hand[3].rank * 15 ** 1
        points = points + hand[4].rank

        return points, 'Straight Flush'

    def is_four_kind(self, hand):
        if hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank:
            points = 8 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 \
                     + hand[3].rank * 15 ** 1 + hand[4].rank
            return points, 'Four of a Kind'
        elif hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank:
            points = 8 * 15 ** 5 + hand[1].rank * 15 ** 4 + hand[2].rank * 15 ** 3 + hand[3].rank * 15 ** 2 \
                     + hand[4].rank * 15 ** 1 + hand[0].rank
            return points, 'Four of a Kind'
        return 0, ''

    def is_full_house(self, hand):
        for i in range(len(hand) - 2):
            if hand[i].rank == hand[i + 1].rank == hand[i + 2].rank:
                points = 7 * 15 ** 5 + hand[i].rank * 15 ** 4 + hand[i + 1].rank * 15 ** 3 + hand[i + 2].rank * 15 ** 2
                if i == 0 and hand[3].rank == hand[4].rank:
                    points += hand[3].rank * 15 ** 1 + hand[4].rank
                    return points, 'Full House'
                elif i == 2 and hand[0].rank == hand[1].rank:
                    points += hand[0].rank * 15 ** 1 + hand[1].rank
                    return points, 'Full House'
        return 0, ''

    def is_flush(self, hand):
        if hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit:
            points = 6 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 \
                     + hand[3].rank * 15 ** 1 + hand[4].rank
            return points, 'Flush'
        return 0, ''

    def is_straight(self, hand):
        rank_order = True
        for i in range(len(hand)-1):
            rank_order = rank_order and hand[i].rank == (hand[i+1].rank + 1)
        if rank_order is False:
            return 0, ''
        points = 5 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 \
            + hand[3].rank * 15 ** 1 + hand[4].rank
        return points, 'Straight'

    def is_three_kind(self, hand):
        for i in range(len(hand) - 2):
            if hand[i].rank == hand[i + 1].rank == hand[i + 2].rank:
                points = 4 * 15 ** 5 + hand[i].rank * 15 ** 4 + hand[i + 1].rank * 15 ** 3 + hand[i + 2].rank * 15 ** 2
                if i == 0:
                    points += hand[3].rank * 15 ** 1 + hand[4].rank
                elif i == 1:
                    points += hand[0].rank * 15 ** 1 + hand[4].rank
                elif i == 2:
                    points += hand[0].rank * 15 ** 1 + hand[1].rank
                return points, 'Three of a Kind'
        return 0, ''

    # determine whether the hand has two pairs
    def is_two_pair(self, hand):
        if hand[0].rank == hand[1].rank:
            if hand[2].rank == hand[3].rank:
                points = 3 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 + \
                         hand[3].rank * 15 ** 1 + hand[4].rank
                return points, 'Two Pair'
            elif hand[3].rank == hand[4].rank:
                points = 3 * 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[3].rank * 15 ** 2 + \
                         hand[4].rank * 15 ** 1 + hand[2].rank
                return points, 'Two Pair'
        elif hand[1].rank == hand[2].rank:
            if hand[3].rank == hand[4].rank:
                points = 3 * 15 ** 5 + hand[1].rank * 15 ** 4 + hand[2].rank * 15 ** 3 + hand[3].rank * 15 ** 2 + \
                         hand[4].rank * 15 ** 1 + hand[0].rank
                return points, 'Two Pair'
        return 0, ''

    def is_one_pair(self, hand):
        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i + 1].rank:
                # determine points (needs to be tweaked)
                points = 2 * 15 ** 5 + hand[i].rank * 15 ** 4 + hand[i+1].rank * 15 ** 3
                if i == 0:
                    points += hand[2].rank * 15 ** 2 + hand[3].rank * 15 ** 1 + hand[4].rank
                elif i == 1:
                    points += hand[0].rank * 15 ** 2 + hand[3].rank * 15 ** 1 + hand[4].rank
                elif i == 2:
                    points += hand[0].rank * 15 ** 2 + hand[1].rank * 15 ** 1 + hand[4].rank
                elif i == 3:
                    points += hand[0].rank * 15 ** 2 + hand[1].rank * 15 ** 1 + hand[2].rank
                return points, 'One Pair'
        return 0, ''

    def is_high_card(self, hand):
        points = 15 ** 5 + hand[0].rank * 15 ** 4 + hand[1].rank * 15 ** 3 + hand[2].rank * 15 ** 2 \
                 + hand[3].rank * 15 ** 1 + hand[4].rank
        return points, 'High Card'


def main():
    # prompt the user to input the number of players
    num_players = int(input('Enter the number of players: '))
    while (num_players < 2) or (num_players > 6):
        num_players = int(input('Enter the number of players: '))
    print()
    # create the Poker object
    game = Poker(num_players)

    # play the game
    game.play()


main()

