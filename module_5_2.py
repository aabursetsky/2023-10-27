class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        i = 1
        if 0 < new_floor <= self.number_of_floors:
            while i <= new_floor:
                print(i)
                i += 1
                continue
        else:
            print("Такого этажа не существует")



# Возвращает кол-во этажей здания
    def __len__(self):
        return(self.number_of_floors)
    
    
# Возвращает строку "Название: <название>, кол-во этажей: <этажи>"
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


# __str__
print(h1)
print(h2)


# __len__
print(len(h1))
print(len(h2))

'''
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20

'''
