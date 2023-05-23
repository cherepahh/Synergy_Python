class box_office():
    x = 0

    def top_up(self, x):
        self.x += x
    
    def count_1000(self):
        print(int(self.x) // 1000)

    def take_away(self, x):
        if self.x < x:
            print('Недостаточно денег')
        else:
            self.x -= x

box = box_office()
box.top_up(10000)
print(box.x)
box.count_1000()
box.take_away(1000.5)
print(box.x)