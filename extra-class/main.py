class Compute:
    def __init__(self, width, height, length):
        self.width = width
        self.height = heigth
        self.length = length

    def area(self):
        self.area = self.width * self*length
        return self.area

    def volume(self):
        self.volume = self.width* self.length* self.height 
        return self.volume

    def display_area(self):
        print(self.area)

    def display_volume(self, volume):
        print(self.volume, volume)

if __name__ == '__main__':

    c = Compute(width=4, heigth=4 , length=4)
    c.area()
    c.volume()
    c.display_area()
    c.display_volume(4)