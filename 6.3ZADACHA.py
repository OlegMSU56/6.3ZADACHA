class Horse:
    def __init__(self, x_distance, y_distance, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self, y_distance, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegas(Horse, Eagle):
    def __init__(self, x_distance, y_distance):
        super().__init__(x_distance, y_distance)


    def move(self, dx, dy):
        return (self.run(dx),self.fly(dy))


    def get_pos(self):
        self.pos = (self.x_distance, self.y_distance)
        return self.pos

    def voice(self):
        print(self.sound)#Почему у нас sound берется от Eagle, если область видимости Horse 'нам ближе' по mro?


p1 = Pegas(0, 0)

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()