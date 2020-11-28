import random


class Player:
    def __init__(self, is_human, is_robot, player_card):
        self.is_human = is_human
        self.is_robot = is_robot
        self.player_card = player_card

    def cross(self, current_ball_from_sack):
        updated_player_card = ['-' if number == current_ball_from_sack else number for number in self.player_card]
        self.player_card = updated_player_card
        return self.player_card

    # def pass_round(self, )


class Sack:
    def __init__(self, current_ball_number):
        self.balls = list(range(1, 91))
        self.current_ball_number = current_ball_number

    def get_current_number(self):
        self.current_ball_number = random.randint(1, 90)
        self.balls.remove(self.current_ball_number)
        return self.current_ball_number


class Card:
    def __init__(self):
        self.card_numbers = random.sample(range(1, 91), 15)

    def print_card(self):
        chunked_card_numbers = list(self.__chunks(self.card_numbers, 5))
        card_rows = []
        for chunk in chunked_card_numbers:
            chunk.sort()
            chunk = [str(n) for n in chunk]
            row = ' '.join(chunk)
            card_rows.append(row)
        card_str = '\n'.join(card_rows)
        print(card_str)

    def __chunks(self, numbers, n):
        for i in range(0, len(numbers), n):
            yield numbers[i:i + n]

    def check_current_number(self, current_number):
        if current_number in self.card_numbers:
            pass
        else:
            print(f'The number {current_number} is not in your card. You lose')


c = Card()
c.print_card()
c.print_card()
