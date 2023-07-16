#Sử dụng hàm tạo __init__()
'''
class Score:
    threshold=4.0
    def __init__(self, point):
      self.point = point
      print("Object with:", point, "has been create!")

score_1 = Score(7.8)
'''

#Xây dựng lớp Circle
class Circle:
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2*self.pi*self.radius
    def areas(self):
        return self.pi*self.radius**2

#Kế thừa trong Python
'''
class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width
        
    def perimeter(self):
        return 2 * (self.l + self.w)
    
    def area(self):
        return self.l * self.w
    
    def display(self):
        print("The length of rectangle is:", self.l)
        print('The width of rectangle is:', self.w)
        print('The perimeter of rectangle is:', self.perimeter())
        print('The area of rectangle is:', self.area())

class Parallelepipede(Rectangle):
    def __init__(self, height, length, width):
        super().__init__(length, width)
        self.h = height
        
    def volume(self):
        return super().area() * self.h
'''
    



