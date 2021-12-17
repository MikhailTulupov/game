from singletons import SingletonMeta


class Field(metaclass=SingletonMeta):
    """
    Игровое поле
    """
    def __init__(self):
        self.START_N = 1
        self.END_N = None
        self.START_M = 1
        self.END_M = None

    def set_field(self, n, m):
        """
        Устанавливаем значения поля
        :param n: значение по вертикали
        :param m: значение по горизонтали
        :return: Field
        """
        self.END_N = n
        self.END_M = m

        return self
