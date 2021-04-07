import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
         if self.direction == "DOWN":
            if self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]+1))).color == consts.fruit_color:
                self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]+1))).set_color(self.color)
                self.cells.append((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]+1)))
            elif self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]+1))).color == consts.back_color:
                self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]+1))).set_color(self.color)
                self.game.get_cell((self.val(self.cells[0][0]),self.val(self.cells[0][1]))).set_color(consts.back_color)
                self.cells.append((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]+1)))
                self.cells.pop(0)
            else:
                self.game.kill(self)
         if self.direction == "UP":
            if self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]-1))).color == consts.fruit_color:
                self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]-1))).set_color(self.color)
                self.cells.append((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]-1)))
            elif self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]-1))).color == consts.back_color:
                self.game.get_cell((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]-1))).set_color(self.color)
                self.game.get_cell((self.val(self.cells[0][0]),self.val(self.cells[0][1]))).set_color(consts.back_color)
                self.cells.append((self.val(self.cells[-1][0]),self.val(self.cells[-1][1]-1)))
                self.cells.pop(0)
            else:
                self.game.kill(self)
               
         if self.direction == "LEFT":
            if self.game.get_cell((self.val(self.cells[-1][0]-1),self.val(self.cells[-1][1]))).color == consts.fruit_color:
                self.game.get_cell((self.val(self.cells[-1][0]-1),self.val(self.cells[-1][1]))).set_color(self.color)
                self.cells.append((self.val(self.cells[-1][0]-1),self.val(self.cells[-1][1])))
            elif self.game.get_cell((self.val(self.cells[-1][0]-1),self.val(self.cells[-1][1]))).color == consts.back_color:
                self.game.get_cell((self.val(self.cells[-1][0]-1),self.val(self.cells[-1][1]))).set_color(self.color)
                self.game.get_cell((self.val(self.cells[0][0]),self.val(self.cells[0][1]))).set_color(consts.back_color)
                self.cells.append((self.val(self.cells[-1][0]-1),self.val(self.cells[-1][1])))
                self.cells.pop(0)
            else:
                self.game.kill(self)  
         if self.direction == "RIGHT":
            if self.game.get_cell((self.val(self.cells[-1][0]+1),self.val(self.cells[-1][1]))).color == consts.fruit_color:
                self.game.get_cell((self.val(self.cells[-1][0]+1),self.val(self.cells[-1][1]))).set_color(self.color)
                self.cells.append((self.val(self.cells[-1][0]+1),self.val(self.cells[-1][1])))
            elif self.game.get_cell((self.val(self.cells[-1][0]+1),self.val(self.cells[-1][1]))).color == consts.back_color:
                self.game.get_cell((self.val(self.cells[-1][0]+1),self.val(self.cells[-1][1]))).set_color(self.color)
                self.game.get_cell((self.val(self.cells[0][0]),self.val(self.cells[0][1]))).set_color(consts.back_color)
                self.cells.append((self.val(self.cells[-1][0]+1),self.val(self.cells[-1][1])))
                self.cells.pop(0)
            else:
                self.game.kill(self)
            
    def handle(self, keys):
        for i in keys:
            if i in self.keys:
                if self.keys[i]=="UP" and self.direction != "DOWN" or self.keys[i]=="DOWN" and self.direction != "UP" or self.keys[i]=="LEFT" and self.direction != "RIGHT" or self.keys[i]=="RIGHT" and self.direction != "LEFT" :
                    
                    self.direction=self.keys[i]
                    #print(self.keys[i])

