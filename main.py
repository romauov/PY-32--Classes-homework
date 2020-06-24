cattle_list = []


class Cattle:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.cattle_data = {self.name: self.weight}
        cattle_list.append(self.cattle_data)
        self.satiety = True  # сытость

    def get_voice(self):
        pass

    def get_name(self):
        print(f'Имя животного {self.name}')
        return self.name

    def get_weight(self):
        print(f'Вес животного {self.name} - {self.weight} кг')
        return self.weight

    def feed(self):
        self.satiety = True
        print(f'Животное {self.name} покормлено')

    # def hunger(self):
    #   self.satiety = False


class Cow(Cattle):
    voice = 'Mooo!'
    milk_amount = 0

    def milk(self):
        self.milk_amount = 0
        print(f'Животное {self.name} подоено')

    def get_voice(self):
        print(self.voice)
        return self.voice


class Goat(Cattle):
    voice = 'Baah!'
    milk_amount = 0

    def milk(self):
        self.milk_amount = 0
        print(f'Животное {self.name} подоено')

    def get_voice(self):
        print(self.voice)
        return self.voice


class Sheep(Cattle):
    wool_amount = 0
    voice = 'Bleat!'

    def wool_cut(self):
        self.wool_amount = 0
        print(f'Животное {self.name} поcтрижено')

    def get_voice(self):
        print(self.voice)
        return self.voice


class Chicken(Cattle):
    egg_amount = 0
    voice = 'Cluck!'

    def egg_gather(self):
        self.egg_amount = 0
        print(f'У животного {self.name} собраны яйца')

    def get_voice(self):
        print(self.voice)
        return self.voice


class Duck(Cattle):
    egg_amount = 0
    voice = 'Quack!'

    def egg_gather(self):
        self.egg_amount = 0
        print(f'У животного {self.name} собраны яйца')

    def get_voice(self):
        print(self.voice)
        return self.voice


class Goose(Cattle):
    egg_amount = 0
    voice = 'Hiss!'

    def egg_gather(self):
        self.egg_amount = 0
        print(f'У животного {self.name} собраны яйца')

    def get_voice(self):
        print(self.voice)
        return self.voice


def total_weight():
    total_weight = 0
    for every_cattle in cattle_list:
        total_weight += list(every_cattle.values())[0]
    print(f'Общий вес животных на ферме - {total_weight} кг')
    return total_weight


def heaviest_weight():
    heaviest_weight = 0
    # heaviest_name = None
    for every_cattle in cattle_list:
        if heaviest_weight < list(every_cattle.values())[0]:
            heaviest_weight = list(every_cattle.values())[0]
            heaviest_name = str(list(every_cattle.keys())[0])
    print(f'самое тяжелое животное на ферме - {heaviest_name}, {heaviest_weight} кг')
    return heaviest_name


goose_white = Goose('White', 4)
goose_grey = Goose('Grey', 5)
cow_manka = Cow('Manka', 498)
chicken_coco = Chicken('Coco', 3)
chicken_doodledoo = Chicken('Doodle-doo', 3)
goat_horns = Goat('Horns', 54)
goat_hooves = Goat('Hooves', 56)
sheep_curly = Sheep('Curly', 36)
sheep_lamb = Sheep('Lamb', 42)
duck_quackly = Duck('Quackly', 4)

total_weight()
heaviest_weight()

cow_manka.milk()
chicken_coco.feed()
goat_horns.get_voice()
sheep_lamb.wool_cut()
goat_horns.milk()
chicken_doodledoo.egg_gather()
goose_grey.egg_gather()
duck_quackly.egg_gather()
sheep_curly.get_weight()
chicken_coco.get_name()

print(cattle_list)

# class Animal:
#     pass
# class Cow(Animal):
#     cattle_data = None
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#     def set_cattle_data(self, var_name):
#         self.cattle_data = {var_name : [self.name, self.weight]}
# class Sheep(Animal):
#     cattle_data = None
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#     def set_cattle_data(self, var_name):
#         self.cattle_data = {var_name : [self.name, self.weight]}
# def get_var_str_name(locals_obj, var_object):
#     return [k for k, v in locals_obj.items() if v == var_object][0]
# animal_1 = Cow('животное 1', 10)
# animal_1.set_cattle_data(get_var_str_name(locals(), animal_1))
# animal_3 = Cow('животное 2', 11)
# animal_3.set_cattle_data(get_var_str_name(locals(), animal_3))
# animal_4 = Sheep('животное 3', 12)
# animal_4.set_cattle_data(get_var_str_name(locals(), animal_4))
# animal_5 = Sheep('животное 4', 13)
# animal_5.set_cattle_data(get_var_str_name(locals(), animal_5))
# animals_list = [animal_1, animal_3, animal_4, animal_5]
# for animal in animals_list:
#     print(animal.cattle_data)