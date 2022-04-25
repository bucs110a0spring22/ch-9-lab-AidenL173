from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, height, width):
    '''
    takes a filename string and saves it to the self.image. Takes x, y coordinates, width, height and creates a rectangle object stored in self.rect
    filename: str, 
    x: int, desired x coordinates
    y: int, desired y coordinates
    height: int, desired height
    width: int, desired width
    '''
    self.image = filename
    self.rect = Rectangle(x, y, height, width)

  def getRect(self):
    '''
    returns the internal rectangle object
    return: Rectangle.Rectangle, the created rectangle object that is stored in self.rect
    '''
    return self.rect