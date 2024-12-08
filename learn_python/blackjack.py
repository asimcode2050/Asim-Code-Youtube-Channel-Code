import random
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 1
}

def deal_card():
    cards = list(card_values.keys())
    return random.choice(cards)

def calculate_hand_value(hand):
    total = 0  # Start with a hand value of 0
    ace_count = 0  # Counter to keep track of the number of Aces in the hand
    for card in hand:
        total += card_values[card]
        if card == 'A':
            ace_count += 1
    while total <= 11 and ace_count > 0:
        total += 10
        ace_count -= 1
    return total


def dealer_turn(dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    return dealer_hand  # Return the final dealer hand after their turn


def player_turn(player_hand):
    while True:
        print(f"Your current hand: {player_hand}, value: {
              calculate_hand_value(player_hand)}")
        action = input("Do you want to hit or stand? ").lower()
        if action == 'hit':
            player_hand.append(deal_card())
            if calculate_hand_value(player_hand) > 21:
                print(f"Busted! Your hand: {player_hand}, value: {
                      calculate_hand_value(player_hand)}")
                return player_hand, True
        elif action == 'stand':
            return player_hand, False
        else:
            print("Invalid choice. Please enter 'hit' or 'stand'.")


def play_blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    print(f"Dealers hand: [{dealer_hand[0]}, ?]")
    player_hand, player_busted = player_turn(player_hand)
    if player_busted:
        print("You busted! Dealer wins.")
        return  # Exit the game
    dealer_hand = dealer_turn(dealer_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Dealers final hand: {dealer_hand}, value: {dealer_value}")
    player_value = calculate_hand_value(player_hand)
    if dealer_value > 21:
        print(f"Dealer busts! Your hand value: {player_value}. You win!")
    elif player_value > dealer_value:
        print(f"Your hand value: {player_value}. You win!")
    elif player_value < dealer_value:
        print(f"Dealer wins with hand value: {
              dealer_value}. Better luck next time!")
    else:
        print(f"Its a tie! Both have a hand value of {player_value}.")


if __name__ == "__main__":
    play_blackjack()
