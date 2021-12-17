import random
from abc import ABC, abstractmethod
from field import Field


class Player(ABC):
    """
    Абстрактный класс Игрока
    """

    def __init__(self, power, health=100):
        self.__position_n = None
        self.__position_m = None
        self.power = power
        self.health = health

    def move(self, enemy_position: tuple[int, int]):
        """
        Предостовляет возможность сделать ход игроку
        :param enemy_position: Текущее местоположение противоположного игрока
        :return: None
        """
        print('Местоположение противника: {0}'.format(enemy_position))
        print('Ваше текущее местоположение:[{0}]'.format(self.get_player_position()))
        print("Сделайте ход:\n")

        move_list = []

        self.step_forward(move_list)
        self.step_left(move_list)
        self.step_right(move_list)
        self.step_back(move_list)
        self.step_diagonally(move_list)

        j = 1
        for item in move_list:
            if tuple(item) == enemy_position:
                continue
            print('{0}) [{1};{2}]\n'.format(j, item[0], item[1]))
            j += 1

        choice = int(input('Ваш выбор: '))

        self.__set_player_position(tuple(move_list[choice - 1]))

    def step_forward(self, move_list: list):
        """
        Предостовляет вариант хода вперед и заполняет список новыми ходами
        :param move_list: список доступных ходов
        :return: Возращает true если можно походить вперед
        """
        if self.__position_n == Field().START_N:
            return False

        move_list.append([self.__position_n - 1, self.__position_m])
        return True

    def step_back(self, move_list: list):
        """
        Предостовляет вариант хода назад и заполняет список новыми ходами
        :param move_list: список доступных ходов
        :return: Возращает true если можно ходить назад
        """
        if self.__position_n == Field().END_N:
            return False

        move_list.append([self.__position_n + 1, self.__position_m])
        return True

    def step_left(self, move_list: list):
        """
        Предостовляет вариант хода влево и заполняет список новыми ходами
        :param move_list: список доступных ходов
        :return: Возращает true если можно ходить назад
        """
        if self.__position_m == Field().START_M:
            return False

        move_list.append([self.__position_n, self.__position_m - 1])
        return True

    def step_right(self, move_list: list):
        """
        Предостовляет вариант хода вправо и заполняет список новыми ходами
        :param move_list: список доступных ходов
        :return: Возращает true если можно ходить назад
        """
        if self.__position_m == Field().END_M:
            return False

        move_list.append([self.__position_n, self.__position_m + 1])
        return True

    def step_diagonally(self, move_list: list):
        """
        Предостовляет варианты ходов по диогонали по четырем направлениям и заполняет список новыми ходами
        :param move_list: список доступных ходов
        :return: Возращает true если можно ходить назад
        """
        # Игрок находится в правом верхнем углу
        if self.__position_m == Field().END_M and self.__position_n == Field().START_N:
            move_list.append([self.__position_n + 1, self.__position_m - 1])
            return True

        # Игрок находится в левом нижнем углу
        elif self.__position_m == Field().START_M and self.__position_n == Field().END_N:
            move_list.append([self.__position_n - 1, self.__position_m + 1])
            return True

        # Игрок находится в правом нижнем углу
        elif self.__position_m == Field().END_M and self.__position_n == Field().END_N:
            move_list.append([self.__position_n - 1, self.__position_m - 1])
            return True
        # Игрок находится в левом верхнем углу
        elif self.__position_m == Field().START_M and self.__position_n == Field().START_N:
            move_list.append([self.__position_n + 1, self.__position_m + 1])
            return True
        # Игрок находится в самой крайней правой стороне поля
        elif self.__position_m == Field().END_M and (
                self.__position_n != Field().START_N and self.__position_n != Field().END_N):
            move_list.append([self.__position_n - 1, self.__position_m - 1])
            move_list.append([self.__position_n + 1, self.__position_m - 1])
            return True
        # Игрок находится в самой крайней левой стороне поля
        elif self.__position_m == Field().START_M and (
                self.__position_n != Field().START_N and self.__position_n != Field().END_N):
            move_list.append([self.__position_n - 1, self.__position_m + 1])
            move_list.append([self.__position_n + 1, self.__position_m + 1])
            return True
        # Игрок находится в самой крайней верхней стороне поля
        elif self.__position_n == Field().START_N and (
                self.__position_m != Field().END_M and self.__position_m != Field().START_M):
            move_list.append([self.__position_n + 1, self.__position_m - 1])
            move_list.append([self.__position_n + 1, self.__position_m + 1])
            return True
        # Игрок находится в самой крайней нижней стороне поля
        elif self.__position_n == Field().END_N and (
                self.__position_m != Field().END_M and self.__position_m != Field().START_M):
            move_list.append([self.__position_n - 1, self.__position_m - 1])
            move_list.append([self.__position_n - 1, self.__position_m + 1])
            return True
        # Игрок находится на месте, где можно походить в любые четыри стороны по диогонали
        else:
            move_list.append([self.__position_n - 1, self.__position_m - 1])
            move_list.append([self.__position_n - 1, self.__position_m + 1])
            move_list.append([self.__position_n + 1, self.__position_m - 1])
            move_list.append([self.__position_n + 1, self.__position_m + 1])
            return True

    @abstractmethod
    def attack(self, enemy_position):
        """
        Предостовляет возможность аттаковать противоположного игрока
        :param enemy_position: Текущее местоположение противоположного игрока
        :return: True если противоположный игрок находится в зоне поражения
        """
        pass

    def random_set_player_position(self):
        """
        Устанавливает позицию игрока в случайном месте
        :return:
        """
        self.__position_n = random.randint(1, Field().END_N)
        self.__position_m = random.randint(1, Field().END_M)
        return self.__position_n, self.__position_m

    def get_player_position(self):
        """
        :return: Возращает текущее местоположение игрока
        """
        return self.__position_n, self.__position_m

    def __set_player_position(self, position: tuple[int, int]):
        self.__position_n, self.__position_m = position


class PlayerA(Player):
    """
    Субкласс от Player. Игрок типа А
    """
    def __init__(self, health=100, power=10):
        super(PlayerA, self).__init__(power, health)

    def attack(self, enemy_position):
        move_list = []
        self.step_forward(move_list)
        self.step_left(move_list)
        self.step_right(move_list)
        self.step_back(move_list)
        self.step_diagonally(move_list)
        for item in move_list:
            if tuple(item) == enemy_position:
                return True
        return False


class PlayerB(Player):
    """
        Субкласс от Player. Игрок типа B
        """

    def __init__(self, health=100, power=20):
        super(PlayerB, self).__init__(power, health)

    def attack(self, enemy_position: tuple):
        move_list = []
        self.step_forward(move_list)
        self.step_left(move_list)
        self.step_right(move_list)
        self.step_back(move_list)
        for item in move_list:
            if tuple(item) == enemy_position:
                return True
        return False

# class PlayerC(Player):
#
#     def __init__(self,power, health=100):
#         super(PlayerC, self).__init__(power,health)


