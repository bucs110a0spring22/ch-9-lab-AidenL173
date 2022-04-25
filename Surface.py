from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    self.image = filename
    self.rect = Rectangle(x, y, h, w)

  def getRect(self):
    '''
    returns the internal rectangle object
    self: str, 
    return: str, 
    '''
    return self.rect