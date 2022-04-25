class Rectangle:
  def __init__(self, x, y, height, width):
    '''
    takes x, y coordinates, width, height and saves them as instance variables
    x: int, desired x coordinates
    y: int, desired y coordinates
    height: int, desired height
    width: int, desired width
    '''
    self.x = x if x > 0 else 0
    self.y = y if y > 0 else 0
    self.height = height if height > 0 else 0
    self.width = width if width > 0 else 0

  def __str__(self):
    '''
    returns a string containing the x, y, width, and height of the rectangle
    return: str, a string containing the x, y, width, and height of the rectangle
    '''
    return "(x:" + str(self.x) + ", y:" + str(self.y) + ") width:" + str(self.width) + ", height:" + str(self.height)