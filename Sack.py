import random

class Player:
    def __init__(self, is_human, is_robot, palyer_card):
        self.is_human = is_human
        self.is_robot = is_robot
        self.palyer_card = palyer_card

    def cross(self, current_ball_from_sack):
        updated_player_card = ['-' if number == current_ball_from_sack else number for number in self.palyer_card]
        self.palyer_card = updated_player_card
        return self.palyer_card


class Sack:
    def __init__(self, current_ball_number):
        self.balls = list(range(1, 91))
        self.current_ball_number = current_ball_number

    def get_current_number(self):
        self.current_ball_number = random.randint(1, 90)
        self.balls.remove(self.current_ball_number)
        return self.current_ball_number


class Card:
    def __init__(self, card_numbers):
        self.card_numbers = []
        i = 1
        while i <= 15:
            n = random.randint(1, 90)
            if n not in self.card_numbers:
                self.card_numbers.append(n)
                i += 1
            continue

    def update_card(self):
        pass


