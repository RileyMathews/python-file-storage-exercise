class Dealership:

    def __init__(self):
        self.car_models = list()
        self.car_makes = list()

    def strip_formating(self, input_list):
        new_list = list()
        for string in input_list:
            new_list.append(string.strip())
        return tuple(new_list)

    def get_car_models(self):
        with open('car_models.txt', 'r') as models:
            self.car_models = self.strip_formating(models.readlines())

    def get_car_makes(self):
        with open('car_makes.txt', 'r') as makes:
            makes = self.strip_formating(makes.readlines())
            self.car_makes = (car.split("=")[1] for car in makes)


    def generate_car_dictionary(self):
        print(dict(zip(self.car_makes, self.car_models)))

auto_ranch = Dealership()
auto_ranch.get_car_makes()
auto_ranch.get_car_models()
auto_ranch.generate_car_dictionary()
