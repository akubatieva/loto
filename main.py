from game_parts import Sack, Card




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player_card = Card()
    sack = Sack()
    while len(sack) != 0:
        current_ball = sack.get_current_number()
        print(f'Новый бочонок: {current_ball} (осталось: {len(sack)})')
        print('------ Ваша карточка -----')
        player_card.print_card()
        print('--------------------------')
        inp = input('Зачеркнуть цифру? (y/n) ')
        if inp == 'y':
            if player_card.contains(current_ball):
                player_card.cross_number(current_ball)
                if player_card.if_everything_crossed():
                    print('Вы выиграли!')
                    break
                continue
            else:
                print(f'В вашей карточке нет числа {current_ball}. Вы проиграли')
                break
        if inp == 'n':
            if player_card.contains(current_ball):
                print(f'В вашей карточке есть число {current_ball}. Вы проиграли')
                break
            else:
                continue




