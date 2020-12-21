import random

NUMBERS_RANGE = range(1, 91)


class Player:
    def __init__(self, player_card, player_id):
        self.player_card = player_card
        self.player_id = player_id

    def should_cross(self, current_ball_from_sack):
        pass


class HumanPlayer(Player):
    def should_cross(self, current_ball_from_sack):
        inp = input(f'Игрок {self.player_id}, зачеркнуть цифру? (y/n) ')
        if inp == 'y':
            return True
        return False


class AIPlayer(Player):
    def should_cross(self, current_ball_from_sack):
        if self.player_card.contains(current_ball_from_sack):
            return True
        return False


class Sack:
    def __init__(self):
        self.balls = list(NUMBERS_RANGE)

    def get_current_number(self):
        current_ball_index = random.choice(range(len(self.balls)))
        current_ball_number = self.balls[current_ball_index]
        del self.balls[current_ball_index]
        return current_ball_number

    def __len__(self):
        return len(self.balls)


class Card:
    def __init__(self):
        card_numbers = random.sample(NUMBERS_RANGE, 15)
        self.card_rows = list(self.__chunks(card_numbers, 5))
        for row in self.card_rows:
            row.sort()
            for i in range(4):
                row.insert(random.randint(0, len(row)), '')

    def __chunks(self, numbers, n):
        for i in range(0, len(numbers), n):
            yield numbers[i:i + n]

    def cross_number(self, number_to_cross):
        updated_rows = []
        for row in self.card_rows:
            updated_row = ['-' if number == number_to_cross else number for number in row]
            updated_rows.append(updated_row)
        self.card_rows = updated_rows
        return self.card_rows

    def contains(self, number):
        for row in self.card_rows:
            if number in row:
                return True
        return False

    def if_everything_crossed(self):
        for row in self.card_rows:
            if not all(number == '-' or number == '' for number in row):
                return False
        return True

    def __str__(self):
        _ = []
        for row in self.card_rows:
            row = [str(n).rjust(3) for n in row]
            row = ' '.join(row)
            _.append(row)
        card_str = '\n'.join(_)
        return card_str
