from game_parts import Sack, Card, HumanPlayer, AIPlayer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sack = Sack()
    players = [HumanPlayer(player_card=Card()), AIPlayer(player_card=Card())]
    while len(sack) != 0:
        current_ball = sack.get_current_number()
        print(f'Новый бочонок: {current_ball} (осталось: {len(sack)})')
        for i, user in enumerate(players, start=1):
            print(f'------ Карточка игрока {i} -----')
            user.player_card.print_card()
            print('--------------------------')

        for i, user in enumerate(players, start=1):
            should_cross = user.should_cross(current_ball)
            if should_cross:
                if user.player_card.contains(current_ball):
                    user.player_card.cross_number(current_ball)
                    if user.player_card.if_everything_crossed():
                        print(f'Игрок {i} выиграл!')
                        break
                else:
                    print(f'В карточке игрока {i} нет числа {current_ball}. Игрок {i} проиграл')
                    break
            else:
                if user.player_card.contains(current_ball):
                    print(f'В карточке игрока {i} есть число {current_ball}. Игрок {i} проиграл')
                    break




