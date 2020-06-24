# Пример с классом который выполняет роль хранилища (пример упрощен)

class AnimalDB:
    """
    Класс хранилище - простецкая база данных, хранит экземпляры классов животных
    """

    def __init__(self):
        self.data = []

    def add_animal(self, animal_instance):
        self.data.append(animal_instance)
        return f'Успешно добавили {animal_instance.name}'

    def get_animal(self):
        for animal in self.data:
            yield animal

    def get_all_animals(self):
        return self.data


class Animals:
    name = ''
    weight = 0
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        return print('omnomnom')

    def speak(self):
        return print(self.voice)


# отдельный класс для птиц
# содержит специфический метод get_eggs
class Birds(Animals):
    def get_eggs(self):
        return print('eggs collected')


# отдельный класс для животах, дающих молоко
# содержит специфический метод get_milk
class MilkyWay(Animals):
    def get_milk(self):
        return print('milk collected')


# создаём класс для каждого животного:
class Goose(Birds):
    # переопределяем атрибут voice для каждого животного в его классе:
    voice = 'gagaga'


class Chicken(Birds):
    voice = 'kokoko'


class Duck(Birds):
    voice = 'quack'


class Cow(MilkyWay):
    voice = 'mooooo'


class Goat(MilkyWay):
    voice = 'beeeee'


class Sheep(Animals):
    voice = 'meeeee'

    def get_wool(self):
        return print('wool collected')


def get_total_weight(data_obj: AnimalDB):
    """
    Расчет общего веса делаем циклом т.к. get_animal это генератор.
    Когда вы пройдетте генераторы, вы сможете это решить одной строкой
    """
    weight = 0
    for animal in data_obj.get_animal():
        weight += animal.weight
    return weight


def get_max_weight_animal_name(data_obj: AnimalDB):
    """
    Расчет делаем циклом т.к. get_animal это генератор
    Когда вы пройдёте генераторы, вы сможете это решить одной строкой
    """
    weight, name = 0, ''
    for animal in data_obj.get_animal():
        if animal.weight > weight:
            weight = animal.weight
            name = animal.name
    return name


animalFarm = AnimalDB()
animalFarm.add_animal(Goose('Серый', 3))
animalFarm.add_animal(Goose('Белый', 2.8))
animalFarm.add_animal(Cow('Манька', 700))
animalFarm.add_animal(Sheep('Барашек', 70))
animalFarm.add_animal(Sheep('Кудрявый', 65))
animalFarm.add_animal(Chicken('Ко-Ко', 2))
animalFarm.add_animal(Chicken('Кукареку', 2.5))
animalFarm.add_animal(Goat('Рога', 80))
animalFarm.add_animal(Goat('Копыта', 90))
animalFarm.add_animal(Duck('Кряква', 4))

if __name__ == '__main__':
    total_weight = get_total_weight(animalFarm)
    print('общий вес всех животных на ферме: ', total_weight)

    animal_name = get_max_weight_animal_name(animalFarm)
    print('самое тяжёлое животное на ферме: ', animal_name)