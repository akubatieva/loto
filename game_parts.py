import random


class Player:
    def __init__(self, is_human, is_robot, player_card):
        self.is_human = is_human
        self.is_robot = is_robot
        self.player_card = player_card

    def cross(self, current_ball_from_sack):
        pass
    # def pass_round(self, )


class Sack:
    def __init__(self):
        self.balls = list(range(1, 91))

    def get_current_number(self):
        current_ball_index = random.choice(range(len(self.balls)))
        current_ball_number = self.balls[current_ball_index]
        del self.balls[current_ball_index]
        return current_ball_number


class Card:
    def __init__(self):
        card_numbers = random.sample(range(1, 91), 15)
        self.card_rows = list(self.__chunks(card_numbers, 5))
        for row in self.card_rows:
            row.sort()

    def __chunks(self, numbers, n):
        for i in range(0, len(numbers), n):
            yield numbers[i:i + n]

    def print_card(self):
        _ = []
        for row in self.card_rows:
            row = [str(n).rjust(3) for n in row]
            row = ' '.join(row)
            _.append(row)
        card_str = '\n'.join(_)
        print(card_str)

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


s = Sack()
for i in range(91):
    print(s.get_current_number())

# c = Card()
# c.print_card()
# c.cross_number(c.card_rows[0][1])
# c.cross_number(c.card_rows[1][3])
# c.cross_number(c.card_rows[2][2])
# print(c.contains(123))
# print(c.contains(c.card_rows[0][3]))
# c.print_card()
