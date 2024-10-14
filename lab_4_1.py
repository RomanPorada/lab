class Scullion:
    __model : str
    __complect : int
    __marca : str
    __costs : int
    def __init__(self, marca = "Невідомо", complect = 1, model = "Невідомо", costs = 1):
        self.__model = model
        self.__marca = marca
        self.__complect = complect
        self.__costs = costs

    def water_consumption(self):
        complect = self.__complect
        costs = self.__costs
        return costs * complect
        

scullion_1 = Scullion("Samsung", 5, "YZ:18", 12)

print(f"На миття ви витратете {scullion_1.water_consumption()} грн")