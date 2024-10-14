class Camera:
    """"
        This class manages objects of type camera
    """

    year_of_manufacture : int
    country_of_manufacture : str
    __manufacturer : str
    __memory_capacity : int
    __zoom_factor : float
    _anonim : int

    def __init__(self, year_of_manufacture = 2024, country_of_manufacture="Невідомо", manufacturer = "Невідомо", memory_capasity = 0, zoom_factor = 1.0, anonim = 1):
        """
            Конструктор який присвоює значення по замовчуванню
        """
        self.year_of_manufacture = year_of_manufacture
        self.country_of_manufacture = country_of_manufacture
        self.__manufacturer = manufacturer
        self.__memory_capacity = memory_capasity
        self.__zoom_factor = zoom_factor
        self._anonim = anonim
    
    def get_manufactyrer(self):
        """
            Метод отримання до виробника
        """
        return self.__manufacturer
    
    def get_memory_capacity(self):
        """
            Метод отримання до обєму пам'яті
        """
        return self.__memory_capacity
    
    def get_zoom_factor(self):
        """
            Метод отримання кратності зуму
        """
        return self.__zoom_factor
    
    def set_manufacrurer(self, manufacture):
        """
            Метод зміни значення виробника
        """
        self.__manufacturer = manufacture

    def set_memory_capacity(self, memory_capacity):
        """
            Метод зміни значення о'бєму пам'яті
        """
        self.__memory_capacity = memory_capacity

    def set_zoom_factor(self, zoom_factor):
        """
            Метод зміни кратності зуму
        """
        self.__zoom_factor = zoom_factor

    def __str__(self):
        """
            Метод перевизначення __str__
        """
        return f"Camera(year of manufacture = {self.year_of_manufacture}, country of manufacture = {self.country_of_manufacture}, manufacturer = {self.__manufacturer}, memory capacity = {self.__memory_capacity}, zoom factor = {self.__zoom_factor}, anonim = {self._anonim})"
    
    def __repr__(self):
        """
            Метод перевизначення __repr__
        """
        return f"Camera({self.year_of_manufacture}, {self.country_of_manufacture}, {self.__manufacturer}, {self.__memory_capacity}, {self.__zoom_factor})"
    
    def __del__(self):
        """
            Деструктор
        """
        print(f"Object is camera {self.__manufacturer} is deleted")

def main():
    camera_1 = Camera(2021, "USA", "Sony", 64000, 3.6, 65)
    camera_2 = Camera(2022, "Japen", "Canon", 32000, 2.5, 12)
    camera_3 = Camera(1998, "Poland", "Nikon", 16000, 5)
    camera_1.year_of_manufacture = 123
    camera_1._anonim = 1776
    print(camera_1)
    print(camera_2)
    print(camera_3)

    print(f"camera 1 manufacturer is {camera_1.get_manufactyrer()}")
    print(f"camera 2 memory capaciti is {camera_2.get_memory_capacity()} MB")
    print(f"camer 3 zoom factor is {camera_3.get_zoom_factor()}")
    

main()