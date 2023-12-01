class Tomato:
    _states = {0: 'flowering', 1: 'early fruiting', 2: 'mid fruiting', 3: 'mature fruiting'}

    # объявление статического атрибута со всеми стадиями помидорки

    def __init__(self, index):
        self._index = index
        self._state = self._states[0]
        # объявление защищенных динамических атрибутов

    def grow(self):
        state_now = list(Tomato._states.values()).index(self._state) + 1
        # определение индекса следующей стадии созревания помидорки
        if state_now > 3:
            state_now = 0
        # проверка на выход за пределы словаря
        self._state = Tomato._states[state_now]
        # новое состояние помидорки
        print(self._state)

    def is_ripe(self):
        if self._state == Tomato._states[3]:
            print(f"Помидор №{self._index} созрел")
        else:
            print(f"Помидор №{self._index} еще не созрел")


class TomatoBush:
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(i) for i in range(amount)]
        # создание списка из объектов класса Tomato

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
        # каждая помидорка растет на 1 стадию

    def all_are_ripe(self):
        count = 0
        for i in self.tomatoes:
            if i._state == Tomato._states[3]:
                count += 1
            # считаем сколько помидорок созрело
            else:
                break
        return count == self.amount  # проверяем все ли созрело (вывод функции булиновское true/false)

    def harvest(self):
        self.tomatoes.clear()
        # чистим список


class Gardener:
    def __init__(self, name, plant):
        self.name = name  # публичный атрибут
        self._plant = plant  # защищенный атрибут

    def work(self):
        self._plant.grow_all()  # растим все на 1 стадию методом класса Tomatobush

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Пора собирать урожай")
        else:
            print("Не пора собирать урожай")

    @staticmethod # для справки подойдет метод, который не работает с экземпляром целиком.
    def knowledge_base(self):
        print(
            f"Дана настоящая в том, что {self.name} являлся с 1964 года по день смерти 21 января 2003 года членом садоводческого некоммерческого товарищества Восход,"
            f" находящегося в массиве Васкелово Всеволожского района Ленинградской области.\n"
            f"{self.name} по праву частной собственности принадлежали возведённые в соответствии с Уставом садовый дом и надворные постройки, которые расположены на "
            f"участке № 10 вышеуказанного садоводческого некоммерческого товарищества Восход.\n"
            f"Земельный участок, на котором находятся названные строения, являлся собственностью {self.name}.\n"
            f"Задолженностей по членским, целевым взносам и налогам за {self.name} в садоводческом некоммерческом товариществе не значится.")


test_bush = TomatoBush(5)
gardener = Gardener("Steph", test_bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.knowledge_base(gardener)
