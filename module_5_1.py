class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.n_floors = number_of_floors

    def go_to(self, n_floor):
        if n_floor > self.n_floors or n_floor < 1:
            print("Такого этажа не существует")
        for i in range(n_floor):
            j = i + 1
            if n_floor < self.n_floors:
                print(j)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(11)
h1.go_to(0)
h1.go_to(-2)

h2.go_to(10)
