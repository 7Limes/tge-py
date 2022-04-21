# Terminal Based Game Engine
# By Miles Burkart
# 4/14/2022

import time
from surf import Surface
from getch import _Getch

_g = _Getch()

class Clock:
  def __init__(self, framerate: int=None):
    self.framerate = framerate
    if framerate != None:
      self.wait = 1 / framerate
  
  def tick(self):
      time.sleep(self.wait)

def get_char():
  return _g()
