# Create a class cuboid , 3 functions area and perimeter and volume
"""
The perimeter of a cuboid is 4(L+B+H).
The volume of a cuboid is LBH.
The total surface area of a cuboid is 2(LB +BH + HL).

"""


class cuboid():
    def __int__(self, l, b, h):
        self.l, b, h = "x"

    def area(self):
        area = 2*l*b+2*b*h+2*h*l
        print("Area of the cuboid is ", area)

    def volume(self):
        volume = l*b*h
        print("Volume of the cuboid is ", volume)

    def perimeter(self):
        perimeter = 4*l+4*b+4*h
        print("Perimeter of the cuboid is ", perimeter)


l = int(input("Length of the cuboid:"))
b = int(input("Breath of the cuboid :"))
h = int(input("Height of the cuboid: "))

objcuboid = cuboid()
objcuboid.area()
objcuboid.volume()
objcuboid.perimeter()


