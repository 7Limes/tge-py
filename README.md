# tge-py
A small game engine using only terminal graphics.

## Initalizing
- Start by creating a `Surface` object with a width and height
- Then fill it with some characters and display it:

```py
import tge

WIDTH, HEIGHT = 5, 5
surf = tge.Surface(WIDTH, HEIGHT)
surf.set_drawchar('.')
surf.fill()
surf.display()
```
Output:
```
. . . . .
. . . . .
. . . . .
. . . . .
. . . . .
```

You can also change the spacing between characters using the `spacing=` keyword argument in the constructor (default is `1`):
```
surf = tge.Surface(WIDTH, HEIGHT, spacing=0)
```
Output:
.....
.....
.....
.....
.....

## Drawing Methods
These methods are all part of the `Surface` class.
`draw_pixel(self, x: int, y: int, char: str=None) -> bool`
`draw_straight_line(self, x: int, y: int, length: int, dir: str) -> bool`
`draw_rect(self, x: int, y: int, width: int, height: int, fill: bool=False)`
`draw_border(self)`
`draw_line(self, x1: int, y1: int, x2: int, y2: int)`
`draw_polygon(self, points: list)`
`draw_ellipse(self, h: int, k: int, a: int, b: int, fill: bool=False)`
`draw_text(self, x: int, y: int, text: str)`
`fill(self)`
`fill_row(self, row: int)`
`fill_col(self, col: int)`
`blit(self, other, x: int, y: int)`

## Changing Characters and Colors
To change the draw character, use the `set_drawchar()` method:
```py
import tge

surf = tge.Surface(5,5)
surf.set_drawchar('#')
surf.draw_border()
surf.display()
```
Output:
```
# # # # #
#       #
#       #
#       #
# # # # #
```

To change pixel color, you can use one of two methods:
- `set_color(self, color: str, type='fg', bright=False)`
- `set_color_rgb(self, r: int, g: int, b: int, type='fg')`
