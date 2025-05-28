import art
import random
def dealer_card():
    """ turns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """takes list of cards and return sum of list elements as score of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0 :
        return "lose , opponent has Blackjack."
    elif u_score == 0 :
        return "win with a Blackjack."
    elif u_score > 21 :
        return "You went over . You Lose ."
    elif c_score >21 :
        return "Opponent went over . You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "you lose."


def play_game():
    print(art.logo)
    user_cards =[]
    computer_card = []
    computer_score = -1
    user_score = -1

    is_game_over = False

    for _ in range(2):
        user_cards.append(dealer_card())
        computer_card.append(dealer_card())
    while not is_game_over :
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_card)
        print(f"your card = {user_cards} , score = {user_score}")
        print(f"Computer's first card :{computer_card[0]}")

        if user_score == 0 or computer_score  == 0 or user_score > 21 :
            is_game_over = True
        else:
            user_should_deal = input("type y to get another card of n to pass")
            if user_should_deal == "y":
                user_cards.append(dealer_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score   < 17:
         computer_card.append(dealer_card())
         computer_score = calculate_score(computer_card)

    print(f"your final hand : {user_cards} , final score = {user_score}")
    print(f"your final hand : {computer_card} , final score = {computer_score}")
    print(compare(user_score , computer_score))

while input("Do you wanna play a game of BlackJack .type y or n."):
    play_game()
