from field import Field
from players import PlayerA, PlayerB
from singletons import SingletonMeta


class Game(metaclass=SingletonMeta):
    """
    Игра
    """

    def __init__(self):
        n, m = map(int, input('Введите размерность поля n x m: ').split(' '))
        self.field = Field().set_field(n, m)
        health, power = map(int, input("Введите здоровье и силу удара для игрока а: ").split(" "))
        self.player_a = PlayerA(health, power)
        health, power = map(int, input("Введите здоровье и силу удара для игрока b: ").split(" "))
        self.player_b = PlayerB(health,power)

    def play(self):
        """
        Запускает игру
        :return: None
        """
        self.initial_players_positions()
        while True:
            if self.player_a.health <= 0:
                print('Победил игрок b!\n')
                break
            elif self.player_b.health <= 0:
                print('Победил игрок a!\n')
                break

            print('Ход игрока a!\n')
            if self.player_a.attack(self.player_b.get_player_position()):
                print('Игрок b в зоне поражения атакуем\n')
                self.player_b.health -= self.player_a.power
                if self.player_b.health <= 0:
                    continue
                print('Здоровье игрока b: ', self.player_b.health)
            else:
                self.player_a.move(self.player_b.get_player_position())

            print('Ход игрока b!\n')
            if self.player_b.attack(self.player_a.get_player_position()):
                print('Игрок a в зоне поражения атакуем\n')
                self.player_a.health = self.player_a.health - self.player_b.power
                if self.player_a.health <= 0:
                    continue
                print('Здоровье игрока a: ', self.player_a.health)
            else:
                self.player_b.move(self.player_a.get_player_position())

    def initial_players_positions(self):
        """
        Устанавливаем начальные позиции для игрока a и b
        :return: None
        """
        while True:
            if self.player_a.random_set_player_position() != self.player_b.random_set_player_position():
                break
