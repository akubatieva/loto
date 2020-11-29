from game_parts import Sack, Card, HumanPlayer, AIPlayer


def play(players, current_ball):
    is_game_ended = False
    for i, user in enumerate(players, start=1):
        should_cross = user.should_cross(current_ball)
        if isinstance(user, AIPlayer) and should_cross:
            print(f'Игрок {i} вычеркнул число {current_ball}')
        if should_cross:
            if user.player_card.contains(current_ball):
                user.player_card.cross_number(current_ball)

                if user.player_card.if_everything_crossed():
                    print(f'Игрок {i} выиграл!')
                    is_game_ended = True
                    break
            else:
                print(f'В карточке игрока {i} нет числа {current_ball}. Игрок {i} проиграл')
                is_game_ended = True
                break
        else:
            if user.player_card.contains(current_ball):
                print(f'В карточке игрока {i} есть число {current_ball}. Игрок {i} проиграл')
                is_game_ended = True
                break
    return is_game_ended


def get_players(players_number):
    players = []
    for i in range(1, players_number + 1):
        player_type = input(f'Игрок {i} - человек или компьютер? Введите 1, если человек, введите 2, если компьютер: ')
        if player_type == '1':
            players.append(HumanPlayer(player_card=Card(), player_id=i))
        if player_type == '2':
            players.append(AIPlayer(player_card=Card(), player_id=i))
    return players


if __name__ == '__main__':
    sack = Sack()
    players_number = int(input('Введите число игроков: '))
    players = get_players(players_number)
    while len(sack) != 0:
        current_ball = sack.get_current_number()
        print()
        print(f'Новый бочонок: {current_ball} (осталось: {len(sack)})')
        for i, user in enumerate(players, start=1):
            print(f'------ Карточка игрока {i} -------')
            print(user.player_card)
            print('---------------------------------')

        if play(players, current_ball):
            break
