class Rectangle:
  def __init__(self, x, y, height, width):
    self.x = x if x > 0 else 0
    self.y = y if y > 0 else 0
    self.height = height if height > 0 else 0
    self.width = width if width > 0 else 0

  def __str__(self):
    return "(x:" + str(self.x) + ", y:" + str(self.y) + ") width:" + str(self.width) + ", height:" + str(self.height)