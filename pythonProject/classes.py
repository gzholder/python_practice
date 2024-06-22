#???????
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

    def set_width(self, width):
        if width <= 0:
            raise ValueError("width must be positive")
        else:
            self.width = width

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width ==other.width and self.height == other.height
        else:
            return NotImplemented

r1 = Rectangle(10, 20)
# print first function
print(r1.area())
print(r1.perimeter())
print(str(r1))
l =[1, 2, 3]
print(str(l))


#print(r1.to_string())
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person('gabriel', 36)
# print(p1.name + " " + str(p1.age))
