class Triangle:
    def __init__(self, triangle1_base, triangle1_height, triangle2_base, triangle2_height):
        self.triangle1_base = triangle1_base
        self.triangle1_height = triangle1_height
        self.triangle2_base = triangle2_base
        self.triangle2_height = triangle2_height
    
    def triangle_area(self):
        triangle1_area = (self.triangle1_base * self.triangle1_height) / 2.0
        triangle2_area = (self.triangle2_base * self.triangle2_height) / 2.0
        
        if (triangle1_area > triangle2_area):
            print('Triangle with larger area:')
            print('Base: {:.2f}'.format(self.triangle1_base))
            print('Height: {:.2f}'.format(self.triangle1_height))
            print('Area: {:.2f}'.format(triangle1_area))
        elif (triangle2_area > triangle1_area):
            print('Triangle with larger area:')
            print('Base: {:.2f}'.format(self.triangle2_base))
            print('Height: {:.2f}'.format(self.triangle2_height))
            print('Area: {:.2f}'.format(triangle2_area))

try:
    triangle1_base = float(input("Enter triangle 1's base: "))
    triangle1_height = float(input("Enter triangle 1's height: "))
    triangle2_base = float(input("Enter triangle 2's base: "))
    triangle2_height = float(input("Enter triangle 2's height: "))
except ValueError:
    print('Incorrect Input')

print('\n')
triangle = Triangle(triangle1_base, triangle1_height, triangle2_base, triangle2_height)
triangle.triangle_area()