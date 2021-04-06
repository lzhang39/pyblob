class Blob:
  def __init__(self, color):
    self.x = random.randrange(0, WIDTH)
    self.y = random.randrange (0, HEIGHT)
    self.size = random.randrange (4,8)
    self.color = color

  def move(self):
    self.move_x = radom.randrange (-1,2)
    self.move_y = random.randrange(-1,2)
    self.x += self.move_x
    self.y += self.move_y