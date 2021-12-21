from math import sqrt

class Shape:
    pi = 3.14159
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # навіщо оголошувати клас в дочірніх класах, якщо він у всіх працює однаково
    def get_center(self):       
        return [self.x, self.y]

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        

class Circle(Shape):
    def __init__(self, x, y, radius=1):
        super().__init__(x, y)
        self.radius = radius


class Square(Shape):
    def __init__(self, x, y, side=1):
        super().__init__(x, y)
        self.side = side

    # вершини квадрату починаючи з лівого верхнього
    #   A B
    #   C D
    def get_vertex(self):
        diff_x = self.x / 2
        diff_y = self.y / 2
        A = [self.x - diff_x, self.y + diff_y]
        B = [self.x + diff_x, self.y + diff_y]
        C = [self.x - diff_x, self.y - diff_y]
        D = [self.x + diff_x, self.y - diff_y]
        return [A, B, C, D]
    
    def get_area(self):
        return self.side * self.side
    

class Triangle(Shape):
    def __init__(self, x, y, side=1):
        super().__init__(x, y)
        self.side = side
        self.height = self.get_height()

    def get_height(self):
        self.small_radius = self.side / sqrt(3)
        self.big_radius = self.small_radius * 2

        return self.small_radius + self.big_radius

    # вершини трикутника починаючи з лівого верхнього
    #    B 
    #   A C
    # Правила по рівносторонньому трикутнику https://www.matem.com.ua/tablepic/1trykutnyky.pdf 
    def get_vertex(self):
        A = [self.x - self.side / 2, self.y - self.small_radius]
        B = [self.x, self.y + self.big_radius]
        C = [self.x + self.side / 2, self.y - self.small_radius]
        
        return [A, B, C]

    # https://sensey.com.ua/yak-znajti-ploshhu-i-storonu-rivnostoronnogo-trikutnika-vpisanogo-v-kolo-formula/ 
    def get_area(self):
        return sqrt(3) / 4 * self.side * self.side


# application 

c1 = Circle(10, 10, 5)
s1 = Square(20, 16, 5)
t1 = Triangle(30, 8, 6)


print("Square:")
print("- center: ", s1.x, s1.y)
print("- side: ", s1.side)
print("- area: ", s1.get_area())
print("- vertex", s1.get_vertex())

print("Tiangle: ")
print("- center: ", t1.x, t1.y)
print("- side: ", t1.side)
print("- area: ", t1.get_area())
print("- vertex: ", t1.get_vertex())


print("The program designed for the forth lesson has been completed!")
