class Turtle():
    x = 0
    y = 0
    s = 1

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s == 1:
            print('Шаг не может быть меньше или равен 0')
        else:
            self.s -= 1

    def count_moves(self, x2, y2):
        if x2 % self.s != 0 or y2 % self.s != 0:
            print('Невозможно достичь указанной координаты')
        else:
            print('Количество шагов: ', abs(x2 // self.s) + abs(y2 // self.s))

turtle = Turtle()
turtle.count_moves(5, 5)
turtle.evolve()
turtle.count_moves(5, 5)
turtle.count_moves(4, 5)
turtle.count_moves(6, 10)