class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "V: " + str(self.x) + "," + str(self.y)
        
    def __add__(self, op2):
        pass

n01 = vector(4, 6)
n02 = vector(2, 2)
n01 = n01 + n02
print(n01)