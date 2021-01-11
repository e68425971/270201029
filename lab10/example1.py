class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.solutionSurface = (self.radius ** 2) * 2 * (3.14) + (self.radius) * 2 * (3.14) * self.height
        self.solutionVolume = (self.radius ** 2) * self.height * (3.14)

    def Surface(self):
        return self.solutionSurface

    def Volume(self):
        return self.solutionVolume


One = Cylinder(2,2)
print(One.solutionVolume)