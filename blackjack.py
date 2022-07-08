import random
# from replit import clear
from art import logo
print(logo)

def blackjack():
    """Blackjack Capstone Project: Each card has the same probability to be selected"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def users_score(user_cards):
        if user_score>10:
            cards[0]=1
        user_cards.append(random.choice(cards))
        return sum(user_cards)
        
    def dealers_score(computer_cards):
        if dealer_score>10 and dealer_score<17:
            cards[0]=1
            computer_cards.append(random.choice(cards))
            return sum(computer_cards)  
        elif dealer_score==21:
            return sum(computer_cards)
        else:
            computer_cards.append(random.choice(cards))
            return sum(computer_cards) 

    def compare(user_score,computer_score):  
        if (user_score>computer_score and user_score<=21) or (user_score<=21 and computer_score>21):
            return "The user wins"
        elif (computer_score>user_score and computer_score<=21) or (user_score>21 and computer_score<=21):
            return "The dealer wins"
        elif user_score==computer_score:
            return "It's a draw"
        elif user_score>21 and computer_score>21:
            return "It's a bust"
        if (user_score==21 and len(user_cards)==2) or (computer_score==21 and len(computer_cards)==2):
            return "Blackjack"
        elif user_score==21 and computer_score==21:
            return "Both Blackjack: The dealer wins."

    user_cards=[random.choice(cards),random.choice(cards)]
    user_score=sum(user_cards)
    computer_cards=[random.choice(cards),random.choice(cards)]
    dealer_score=sum(computer_cards)

    end_game=False
    while not end_game:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score>=21 :
            end_game=True
        else:
            question=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if question=='n':
                end_game=True
            else:
                user_score=users_score(user_cards)
                dealer_score=dealers_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {dealer_score}")

    print(compare(user_score,dealer_score))

new_game=False
while not new_game:
    question=input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()
    if question=='y':
        # clear()
        print(logo)
        blackjack()
    else:
        new_game=True
        # clear()
        print(logo)
        print("Bye Bye")


