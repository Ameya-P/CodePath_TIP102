class Dog:
    def __init__(self, size):
        self.size = size
    
    def makeNoise(self):
        if self.size < 19:
            print("yip!")
        elif self.size < 30:
            print("bark.")
        else:
            print("wooooof!")
    
    def maxDog(d1, d2):
        if d1.size > d2.size:
            return d1
        else:
            return d2
    
    def maxDog(self, d2):
        if self.size > d2.size:
            return self
        else:
            return d2

if __name__ == "__main__":
    d = Dog(50)
    c = Dog(25)
    a = Dog(1)

    Dog.maxDog(d, c).makeNoise()

    c.maxDog(c).makeNoise()

    [d, c, a][0].makeNoise()
    