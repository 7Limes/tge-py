import math
import os

SL_DIRS = {'r': lambda x,y: (x+1,y), 'l': lambda x,y: (x-1,y), 'd': lambda x,y: (x,y+1), 'u': lambda x,y: (x,y-1)}

COLORS = ['black','red','green','yellow','blue','magenta','cyan','white']

def distance(x1, y1, x2, y2):
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def cls():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

class Surface:
  def __init__(self, width: int, height: int, spacing: int=1):
    self.width = width
    self.height = height

    self.screen = [[' ' for i in range(width)] for j in range(height)]
    self.spacing = ' '*spacing
    
    self._drawchar = ' '
    self._color = ''

  def display(self, clear=False):
    if clear:
      cls()
    for row in self.screen:
      print(self.spacing.join(row))

  def set_drawchar(self, c: str):
    self._drawchar = c[0]

  def set_color_rgb(self, r: int, g: int, b: int, type='fg'):
    if type == 'fg':
      self._color = f'\033[38;2;{r};{g};{b}m'
    if type == 'bg':
      self._color = f'\033[48;2;{r};{g};{b}m'

  def set_color(self, color: str, type='fg', bright=False):
    add = 30
    if type == 'bg':
      add = 40
    if bright:
      add += 60
    if color in set(COLORS):
      self._color = f'\033[{add+COLORS.index(color)}m'
    if color == 'reset':
      self._color = '\033[0m'

  def draw_pixel(self, x: int, y: int, char: str=None) -> bool:
    if x >= 0 and x < self.width and y >= 0 and y < self.height:
      if not char or char == '':
        char = self._drawchar
      self.screen[y][x] = self._color+char
      return True
    return False

  def draw_straight_line(self, x: int, y: int, length: int, dir: str) -> bool:
    if dir not in set(SL_DIRS.keys()):
      return False
    f = SL_DIRS[dir]
    for i in range(length):
      self.draw_pixel(x, y)
      x, y = f(x, y)
    return True

  def draw_rect(self, x: int, y: int, width: int, height: int, fill: bool=False):
    if fill:
      for i in range(width):
        self.draw_straight_line(x+i, y, height, 'd')
    else:
      self.draw_straight_line(x, y, width, 'r')
      self.draw_straight_line(x, y+height-1, width, 'r')
      self.draw_straight_line(x, y+1, height-2, 'd')
      self.draw_straight_line(x+width-1, y+1, height-2, 'd')

  def draw_border(self):
    self.draw_rect(0, 0, self.width, self.height)

  def draw_line(self, x1: int, y1: int, x2: int, y2: int):
    if x1 == x2:
      self.draw_straight_line(x1, y1, y2-y1+1, 'd')
      return True
    if y1 == y2:
      self.draw_straight_line(x1, y1, x2-x1+1, 'r')
      return True

    dist = distance(x1, y1, x2, y2)
    dx = (x2-x1)/dist
    dy = (y2-y1)/dist
    x, y = x1, y1
    for i in range(round(dist)):
      if not self.draw_pixel(round(x), round(y)):
        break
      x += dx
      y += dy
    self.draw_pixel(x2, y2)

  def draw_polygon(self, points: list):
    for i in range(len(points)):
      next = i+1
      if next >= len(points):
        next = 0
      self.draw_line(points[i][0], points[i][1], points[next][0], points[next][1])

  def draw_ellipse(self, h: int, k: int, a: int, b: int, fill: bool=False):
    for i in range(a*2+1):
      shiftedx = round(i+(h-a))
      y = b/a * math.sqrt(abs(a**2 - (shiftedx-h)**2))+k
      if fill:
        self.draw_straight_line(shiftedx, round(y), abs(2*(k-round(y)))+1, 'u')
      else:
        self.draw_pixel(shiftedx, round(y))
        self.draw_pixel(shiftedx, round(y) + 2*(k-round(y)))

  def draw_text(self, x: int, y: int, text: str):
    for c in text:
      if not self.draw_pixel(x, y, char=self._color+c):
        break
      x += 1

  def fill(self):
    self.screen = [[self._color+self._drawchar for i in range(self.width)] for j in range(self.height)]

  def fill_row(self, row: int):
    if row >= 0 and row < len(self.screen):
      self.screen[row] = [self._color+self._drawchar] * len(self.screen[0])

  def fill_col(self, col: int):
    if col >= 0 and col < len(self.screen[0]):
      for i in range(len(self.screen)):
        self.screen[i][col] = self._color+self._drawchar

  def blit(self, other, x: int, y: int):
    for i, row in enumerate(other.screen):
      for j, c in enumerate(row):
        if c == ' ':
          continue
        if not self.draw_pixel(x+j, y+i, char=c):
          break
